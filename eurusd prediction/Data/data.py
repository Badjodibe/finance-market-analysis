import pandas as pd
import numpy as np
import yfinance as yf
import pyspark
import matplotlib.pyplot as plt

symbole = "EURUSD=X"
st = "2021-08-01"
et = "2022-06-30"
ste = "2022-07-01"
ete = "2023-02-28"
se = "2023-03-01"
ee = "2023-06-01"

train = yf.download(symbole, start= st, end=et, interval="1h")
test = yf.download(symbole, start=ste, end=ete, interval="1h")
eval_ = yf.download(symbole, start=se, end=ee, interval="1h")

train = train.reset_index()
test = test.reset_index()
eval_ = eval_.reset_index()

train.to_csv("train.csv")
test.to_csv("test.csv")
eval_.to_csv("eval.csv")