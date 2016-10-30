import numpy
import matplotlib
import pandas as pd
import quandl as q

data = q.get("WIKI/GOOGL")

#print(data.head())

data = data[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
data['HL_PCT'] = (data['Adj. High'] - data['Adj. Close']) / data['Adj. Close'] * 100.0
data['PCT_change'] = (data['Adj. Close'] - data['Adj. Open']) / data['Adj. Open'] * 100.0
data = data[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

print(data.head())
