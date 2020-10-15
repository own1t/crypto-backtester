## Back Testing App for CryptoCurrency with RSI Indicator

### Built with Python

### Requirements

- numpy
- python-binance
- TA-Lib
- backtrader

### Documents

### Python-Binance

https://python-binance.readthedocs.io/en/latest/

### Binance Web Socket

https://python-binance.readthedocs.io/en/latest/websockets.html

https://github.com/binance-exchange/binance-official-api-docs/blob/master/web-socket-streams.md

### TA-Lib

https://mrjbq7.github.io/ta-lib/

### Backtrader

https://www.backtrader.com/docu/

### Instruction

- Get API Keys from Binance first

- Create config.py and put your own API keys in

- Fill up the information according to what kind of dataset you would like to get in get_data.py

- Run get_data.py to create csv file

- Run ta.py file to get RSI

- Select the from date, to date, and csv file from backtest.py

- Run backtest.py
