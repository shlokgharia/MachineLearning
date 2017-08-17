import csv_utilities as cu

df = cu.getDfFromExcel("fundamentals", "fundamentals")
# df.set_index('Index')
df['Period Ending'] = df['Period Ending'].map(lambda x: x.year)
# print df.columns.values

df['Book value'] = df['Total Assets'] - df['Total Liabilities'] - df['Intangible Assets']
df['Pre-process Price to book ratio'] = df['Book value']/df['Estimated Shares Outstanding']
df['Total debt to equity'] = df['Total Liabilities']/(df['Total Assets'] - df['Total Liabilities'])

X = df[['Ticker Symbol','Period Ending', 'Estimated Shares Outstanding', 'Current Ratio', 'Book value', 'Pre-process Price to book ratio','Operating Margin', 'Quick Ratio', 'Total debt to equity', 'Earnings Per Share']]
# X.fillna(0, inplace=True)
# X['Price to earnings ratio'] = X['Earnings Per Share']
print X
