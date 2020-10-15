import config
import csv
from binance.client import Client

# https://python-binance.readthedocs.io/en/latest/index.html
# docs for python-binance api

client = Client(config.API_KEY, config.API_SECRET)

# get all symbols and prices
# tickers = client.get_all_tickers()

# for ticker in tickers:
#     print(ticker)

csvfile = open("2017-2020_1hour.csv", "w", newline="")
candlestick_writer = csv.writer(csvfile, delimiter=",")

# receiving historical data from 1 Dec, 2017 which when Binance Market's opened til today's date

# you can change the ticker to check other cryptocurrencies
# you can change the candlestick time period

# KLINE_INTERVAL_1MINUTE = '1m'
# KLINE_INTERVAL_3MINUTE = '3m'
# KLINE_INTERVAL_5MINUTE = '5m'
# KLINE_INTERVAL_15MINUTE = '15m'
# KLINE_INTERVAL_30MINUTE = '30m'
# KLINE_INTERVAL_1HOUR = '1h'
# KLINE_INTERVAL_2HOUR = '2h'
# KLINE_INTERVAL_4HOUR = '4h'
# KLINE_INTERVAL_6HOUR = '6h'
# KLINE_INTERVAL_8HOUR = '8h'
# KLINE_INTERVAL_12HOUR = '12h'
# KLINE_INTERVAL_1DAY = '1d'
# KLINE_INTERVAL_3DAY = '3d'
# KLINE_INTERVAL_1WEEK = '1w'
# KLINE_INTERVAL_1MONTH = '1M'

candlesticks = client.get_historical_klines(
    "BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 Dec, 2017", "14 Oct, 2020")

for candlestick in candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()
