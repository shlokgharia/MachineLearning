import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.random.rand(3,2), columns=['A', 'B'])
df['C'] = df['A']/df['B']
print df[['A', 'B', 'C']]

