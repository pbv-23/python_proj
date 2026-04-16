import matplotlib.pyplot as plt
def plot_weather(df):
   plt.figure()
   plt.plot(df["date"], df["temperature"], label="Temperature")
   plt.plot(df["date"], df["humidity"], label="Humidity")
   plt.xlabel("Date")
   plt.ylabel("Values")
   plt.title("Weather Trends")
   plt.legend()
   plt.show()
# import matplotlib.pyplot as plt
# def plot_weather(df):
#    plt.figure()
#    plt.plot(df["date"], df["temperature"], label="Temperature")
#    plt.plot(df["date"], df["humidity"], label="Humidity")
#    plt.xlabel("Date")
#    plt.ylabel("Values")
#    plt.title("Weather Trends")
#    plt.legend()
#    plt.show()