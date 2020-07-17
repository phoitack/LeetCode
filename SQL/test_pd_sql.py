import pandas as pd
import pandas.io.sql as sqlio
import psycopg2

import numpy as np

from sklearn.metrics import accuracy_score,roc_curve,confusion_matrix
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.model_selection import train_test_split

from pdpbox import pdp,info_plots
#pdp_iso = pdp.pdp_isolate(model)


#conn = psycopg2.connect("host='{}' port={} dbname='{}' user={} password={}".format(host, port, dbname, username, pwd))
#sql = "select count(*) from table;"
#dat = sqlio.read_sql_query(sql, conn)
#conn = None

df = pd.read_csv('/Users/phoitack/Dropbox/Research/Machine_Learning/Data_Masked_Case_Studies/Projects/data/cc_info.csv')

print(df.head())
