import pandas as pd

df = pd.read_csv('Lit-Functions.csv')

#If the source does not have a numbered ID field as the first column, use the line below.
#df.insert(0, 'ID', df.reset_index().index)

print(df.to_string())

df.to_json('json.txt', orient='records')