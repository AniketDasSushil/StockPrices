import pandas_datareader.data as web
import datetime
import pandas as pd
from functools import reduce

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
start = datetime.datetime(2019,9,15)
end = datetime.datetime.now()
ticker ='MSFT'
def get_stock(ticker):
    data = web.DataReader(ticker,'quandl',start,end)
    data[ticker] = data["Close"]
    data = data[[ticker]] 
    return print(round(data,2))
def combine_stocks(tickers):
    data_frames = []
    for i in tickers:
        data_frames.append(get_stock(i))
        
    df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['Date'], how='outer'), data_frames)
    return df_merged


stocks = ["MRNA", "PFE", "JNJ", "GOOGL", 
          "FB", "AAPL", "COST", "WMT", "KR", "JPM", 
          "BAC", "HSBC"]
portfolio = combine_stocks(stocks)
portfolio.to_csv("portfolio.csv")