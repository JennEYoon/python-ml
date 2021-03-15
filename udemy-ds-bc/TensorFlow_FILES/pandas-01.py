# Pandas test 

import pandas as pd  
df = read_csv('test.csv')

def func(filter, df):  
  df2 = df[filter]
  return df2 

filter = (df['bankruptcies'] > 0)
result = func(filter, df)
result.head() 
# expect 5 rows filtered that meets condition, col bankruptcies > 0 .
