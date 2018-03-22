#!/usr/bin/env python

import pandas as pd

df = pd.read_csv('sales.csv') \
     .rename(columns={
         'Year': 'year',
         'Ready Mix': 'readyMix',
         'Merchant': 'merchant',
         'Products': 'precast',
         'Other': 'other',
     }) \
     .drop(['TOTAL'], axis='columns')

df = pd.melt(df, id_vars=['year'], var_name='channel', value_name='sales')
df['sales'] *= 1e6  # thousand tonnes to kg
df.loc[df.year < 2015, 'region'] = 'GB'
df.loc[df.year >= 2015, 'region'] = 'UK'

df.to_csv('sales_long.csv', index=False)
