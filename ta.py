import talib
import numpy
from numpy import genfromtxt

my_data = genfromtxt("2017-2020_1hour.csv", delimiter=",")

print(my_data)

close = my_data[:, 4]

print(close)

rsi = talib.RSI(close)

print(rsi)
