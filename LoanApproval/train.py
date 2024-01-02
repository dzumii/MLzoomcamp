#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_extraction import DictVectorizer

output_file = 'LoanModel.bin'

data=pd.read_csv("./bankloan.csv")

data.columns = data.columns.str.lower().str.replace('.', '_')

df_full_train, df_test = train_test_split(data, test_size=0.2, random_state=1)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_full_train.personal_loan.values
y_test = df_test.personal_loan.values

del df_full_train['personal_loan']
del df_test['personal_loan']

dv = DictVectorizer(sparse=False)

train_dict = df_full_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

test_dict = df_test.to_dict(orient='records')
X_test = dv.transform(test_dict)

model = DecisionTreeClassifier(max_depth=10,
                                       min_samples_split=50,
                                       min_samples_leaf=20,
                                        random_state=1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print ('RMSE:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}')