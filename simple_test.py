import pandas as pd
import numpy as np
import csv_utilities as cu
# df = pd.DataFrame(data=np.random.rand(3,2), columns=['A', 'B'])
# df['C'] = df['A']/df['B']
# print df[['A', 'B', 'C']]
# price_data = pd.read_csv('fundamentals.csv', sep=",")
# print price_data['Period Ending']


price_data = pd.read_csv('stock_prices_new.txt', sep=" ", header=None, names=["Ticker Symbol", "Period Ending", "price_begin", "price_end"])
# price_data.columns = ["Ticker Symbol", "Period Ending", "price_begin", "price_end"]
price_data.set_index(['Ticker Symbol', 'Period Ending'])

df = cu.getDfFromExcel("fundamentals", "fundamentals")
df['Period Ending'] = df['Period Ending'].map(lambda x: x.year)
df.set_index(['Ticker Symbol', 'Period Ending'])

result = pd.concat([df, price_data], axis=1)
print result

