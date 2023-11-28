import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import  mean_squared_log_error as mse
import pickle as pick

with open("linear_model.pck", "rb") as fichier:
    linear = pick.load(fichier)
eval = pd.read_csv("../Data/eval_prepared.csv")


def target_train(data):

    X = pd.DataFrame()
    y = pd.DataFrame()
    y = data["Target"]
    X = data.drop(columns="Target")
    return X, y


X_eval, y_eval = target_train(eval)
predict = linear.predict(X_eval)
print(predict[1:19])
