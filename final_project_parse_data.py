import csv_utilities as cu
import pandas as pd

df = cu.getDfFromExcel("fundamentals", "fundamentals")
df['Period Ending'] = df['Period Ending'].map(lambda x: x.year)
df.set_index(['Ticker Symbol', 'Period Ending'])
# print df.columns.values

df['Book value'] = df['Total Assets'] - df['Total Liabilities'] - df['Intangible Assets']
df['Pre-process Price to book ratio'] = df['Book value']/df['Estimated Shares Outstanding']
df['Total debt to equity'] = df['Total Liabilities']/(df['Total Assets'] - df['Total Liabilities'])

X = df[['Ticker Symbol','Period Ending', 'Estimated Shares Outstanding', 'Current Ratio', 'Book value', 'Pre-process Price to book ratio','Operating Margin', 'Quick Ratio', 'Total debt to equity', 'Earnings Per Share']]
print X
X.to_excel('PreprocessXa.xlsx',sheet_name='PreProc_Xa', index = False)
price_data = pd.read_csv('stock_prices_new.txt', sep=" ", header=None, names=["Ticker Symbol", "Period Ending", "price_begin", "price_end"])

X_and_price_data = pd.merge(X, price_data, on=['Ticker Symbol', 'Period Ending'])
X_and_price_data.to_excel('X_and_price_data.xlsx',sheet_name='X_and_price_data', index = False)

