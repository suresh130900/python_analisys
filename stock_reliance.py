import pandas as pd
import matplotlib.pyplot as plt

#loading the Data
reliance = pd.read_csv("RELIANCE.NS.csv")
#priting
print(reliance)

#here we are converting the Date time format
reliance["Date"] =pd.to_datetime(reliance.Date)
print(reliance)

#Setting the Date as the Index
reliance = reliance.set_index("Date")
print(reliance)

#plotting the graph with reagarding to the Closing Price
reliance["Close"].plot(legend= True,figsize=(15,10)) 

plt.show()
