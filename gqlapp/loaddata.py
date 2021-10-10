import sqlite3
import pandas as pd

db_path = '/Users/azadeh/Desktop/graphexample/db.sqlite3'

conn = sqlite3.connect(db_path)
df = pd.read_csv('/Users/azadeh/Desktop/graphexample/sam.csv')


#Set id as index
df['id'] = df.index

#DF columns
df=df[['id', 'Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold']]


#Connect to DB, if the Product Table exists with data, replace it with the data imported
df.to_sql('gqlapp_product', conn, if_exists='replace', index=False)

