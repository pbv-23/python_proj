import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
def analyze_trend(df):
   return {
       "avg_temp": df["temperature"].mean(),
       "max_temp": df["temperature"].max(),
       "min_temp": df["temperature"].min()
   }
def predict_temperature(df, days=1):
   df["day"] = np.arange(len(df))
   X = df[["day"]]
   y = df["temperature"]
   model = LinearRegression()
   model.fit(X, y)
   future_day = [[len(df) + days]]
   return round(model.predict(future_day)[0], 2)
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import numpy as np
# def analyze_trend(df):
#    return {
#        "avg_temp": df["temperature"].mean(),
#        "max_temp": df["temperature"].max(),
#        "min_temp": df["temperature"].min()
#    }
# def predict_temperature(df, days=1):
#    df["day"] = np.arange(len(df))
#    X = df[["day"]]
#    y = df["temperature"]
#    model = LinearRegression()
#    model.fit(X, y)
#    future_day = [[len(df) + days]]
#    return round(model.predict(future_day)[0], 2)