import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50

import pandas_datareader as pdr


tsla = pdr.DataReader('tsla', data_source='yahoo',start='2017-1-1')
print(tsla.head(8))

tsla_close = tsla['Close']
tsla_cummax = tsla_close.cummax()
print(tsla_cummax.head(8))

tsla_trailing_stop = tsla_cummax * .9
print(tsla_trailing_stop.head(8))

def set_trailing_loss(symbol, purchase_date, perc):
    close = pdr.DataReader(symbol, 'yahoo', start=purchase_date)['Close']
    return close.cummax() * perc

msft_trailing_stop = set_trailing_loss('msft', '2017-6-1', .85)
print(msft_trailing_stop.head())
