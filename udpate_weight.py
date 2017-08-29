import csv_utilities as cu
import pandas as pd
import numpy as np

SP500_IDX_2013 = 0.29
SP500_IDX_2014 = 0.11
SP500_IDX_2015 = -0.01

df = cu.getDfFromExcel("fundamentals", "fundamentals")
df['Period Ending'] = df['Period Ending'].map(lambda x: x.year)
df.set_index(['Ticker Symbol', 'Period Ending'])
# print df.columns.values

df['Book value'] = df['Total Assets'] - df['Total Liabilities'] - df['Intangible Assets']
df['Pre-process Price to book ratio'] = df['Book value']/df['Estimated Shares Outstanding']
df['Total debt to equity'] = df['Total Liabilities']/(df['Total Assets'] - df['Total Liabilities'])

X = df[['Ticker Symbol','Period Ending', 'Estimated Shares Outstanding', 'Current Ratio', 'Book value', 'Pre-process Price to book ratio','Operating Margin', 'Quick Ratio', 'Total debt to equity', 'Earnings Per Share']]
# print X
X.to_excel('PreprocessXa.xlsx',sheet_name='PreProc_Xa', index = False)
price_data = pd.read_csv('stock_prices_new.txt', sep=" ", header=None, names=["Ticker Symbol", "Period Ending", "price_begin", "price_end"])

# Class label
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
print type(label)
price_data['Class Label'] = pd.Series(label, index=price_data.index)

# Finsih class label

X_and_price_data = pd.merge(X, price_data, on=['Ticker Symbol', 'Period Ending'])
X_and_price_data['Market capitalization'] = X_and_price_data['Estimated Shares Outstanding']*X_and_price_data['price_end']
X_and_price_data['Price to book ratio'] = X_and_price_data['price_end']/X_and_price_data['Pre-process Price to book ratio']
X_and_price_data['Price to earnings ratio'] = X_and_price_data['price_end']/X_and_price_data['Earnings Per Share']
X_and_price_data.to_excel('X_and_price_data.xlsx',sheet_name='X_and_price_data', index = False)

Xa = X_and_price_data[['Market capitalization', 'Current Ratio', 'Book value', 'Price to book ratio', 'Operating Margin', 'Quick Ratio', 'Total debt to equity', 'Earnings Per Share', 'Price to earnings ratio', 'Class Label']]
Xa.to_excel('X_a_With_Class_Label.xlsx',sheet_name='X_a_With_Class_Label', index = False)