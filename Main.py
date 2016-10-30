import numpy
import matplotlib
import pandas as pd
import quandl as q

data = q.get("WIKI/GOOGL")

print(data.head())