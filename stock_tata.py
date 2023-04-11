import pandas as pd
from matplotlib import pyplot as sys

tata = pd.read_csv("TATAELXSI.NS.csv")
print(tata)

tata["Close"].plot()

sys.show()