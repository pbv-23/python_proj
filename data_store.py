import pandas as pd
import os
FILE_NAME = "weather_data.csv"
def save_data(weather):
   df = pd.DataFrame([weather])
   if os.path.exists(FILE_NAME):
       df.to_csv(FILE_NAME, mode='a', header=False, index=False)
   else:
       df.to_csv(FILE_NAME, index=False)
def load_data():
   if os.path.exists(FILE_NAME):
       return pd.read_csv(FILE_NAME)
   return pd.DataFrame()
# import pandas as pd
# import os
# FILE_NAME = "weather_data.csv"
# def save_data(weather):
#    df = pd.DataFrame([weather])
#    if os.path.exists(FILE_NAME):
#        df.to_csv(FILE_NAME, mode='a', header=False, index=False)
#    else:
#        df.to_csv(FILE_NAME, index=False)
# def load_data():
#    if os.path.exists(FILE_NAME):
#        return pd.read_csv(FILE_NAME)
#    return pd.DataFrame()