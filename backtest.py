import backtrader as bt
import datetime


class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy(size=1)

        if self.rsi > 70 and self.position:
            self.close()


cerebro = bt.Cerebro()

# you can change from date and to date to view selected period of time you want
fromdate = datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2020-10-14', '%Y-%m-%d')

data = bt.feeds.GenericCSVData(dataname="2017-2020_1hour.csv",
                               dtformat=2, compression=60, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)

cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)

cerebro.run()

cerebro.plot()
