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

# print price_data

# df = cu.getDfFromExcel("fundamentals", "fundamentals")
# df['Period Ending'] = df['Period Ending'].map(lambda x: x.year)
# df.set_index(['Ticker Symbol', 'Period Ending'])
#
# result = pd.merge(df, price_data, on=['Ticker Symbol', 'Period Ending'])
# print result.head(5)

SP500_IDX_2013 = 0.29
SP500_IDX_2014 = 0.11
SP500_IDX_2015 = -0.01


price_data = pd.read_csv('stock_prices_new.txt', sep=" ", header=None, names=["Ticker Symbol", "Period Ending", "price_begin", "price_end"])
print "shape: ", price_data.shape
# get class label.
price_data['precent_increase'] = (price_data['price_end'] - price_data['price_begin'])/price_data['price_begin']
label = np.zeros(price_data.shape[0])
for index, row in price_data.iterrows():
    if row['Period Ending'] == 2013:
        if (row['precent_increase'] - SP500_IDX_2013) >= 0.0:
            label[index] = 1
        else:
            label[index] = -1
    if row['Period Ending'] == 2014:
        if (row['precent_increase'] - SP500_IDX_2014) >= 0.0:
            label[index] = 1
        else:
            label[index] = -1
    if row['Period Ending'] == 2015:
        if (row['precent_increase'] - SP500_IDX_2015) >= 0.0:
            label[index] = 1
        else:
            label[index] = -1
print (type(label))
price_data['Class Label'] = pd.Series(label, index=price_data.index)
price_data.to_excel('prices.xlsx',sheet_name='price', index = False)
