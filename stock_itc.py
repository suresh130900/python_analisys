import pandas as pd
from matplotlib import pyplot as sys

itc = pd.read_csv("ITC.NS.csv")
print(itc)

itc['Close'].plot()
sys.show()