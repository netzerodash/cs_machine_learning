import numpy
import matplotlib
import pandas as pd
import Quandl

data = Quandl.get("WIKI/GOOGL")

print(data.head())