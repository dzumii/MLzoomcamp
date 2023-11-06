#!/usr/bin/env python
# coding: utf-8

import pickle
import pandas as pd
import numpy as np
import xgboost as xgb

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_extraction import DictVectorizer

output_file = 'SalariesModel.bin'

salaries=pd.read_csv("./data-science-salaries-2023/ds_salaries.csv")

salaries.columns = salaries.columns.str.lower().str.replace(' ', '_')

salaries["salary"]=np.log1p(salaries.salary.values)

df_full_train, df_test = train_test_split(salaries, test_size=0.2, random_state=1)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_full_train.salary.values
y_test = df_test.salary.values

del df_full_train['salary']
del df_test['salary']

dv = DictVectorizer(sparse=False)

train_dict = df_full_train.to_dict(orient='records')
X_train = dv.fit_transform(train_dict)

test_dict = df_test.to_dict(orient='records')
X_test = dv.transform(test_dict)

features = list(dv.get_feature_names_out())
features

dtrain = xgb.DMatrix(X_train, label=y_train, feature_names=features)
dtest = xgb.DMatrix(X_test, label=y_test, feature_names=features)

watchlist = [(dtrain, 'train'), (dtest, 'test')]

get_ipython().run_cell_magic('capture', 'output', "\nxgb_params = {\n    'eta': 0.85, \n    'max_depth': 6,\n    'min_child_weight': 1,\n\n    'objective': 'reg:squarederror',\n    'nthread': 8,\n\n\n    'seed': 1,\n    'verbosity': 1,\n}\n\nmodel = xgb.train(xgb_params, dtrain, num_boost_round=100)\ny_pred = model.predict(dtest)")

print ('RMSE:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}')



