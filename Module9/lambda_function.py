#!/usr/bin/env python
# coding: utf-8

import numpy as np
import tflite_runtime.interpreter as tflite

from io import BytesIO
from urllib import request
from PIL import Image

#interprete the model predictions
interpreter = tflite.Interpreter(model_path='bees-wasps.h5.tflite')
interpreter.allocate_tensors()
input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

classes = [
    'bees',
    'wasp']

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocess_input(x):
    x=x*1/255.
    return x

target_size = (150,150)
def predict(url):
    downloaded_img=download_image(url)
    prepared_img=prepare_image(downloaded_img, target_size)
    x = np.array(prepared_img,dtype='float32')
    X = preprocess_input(x)
    X = np.expand_dims(X, axis=0)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return dict(zip(classes, float_predictions))


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result


