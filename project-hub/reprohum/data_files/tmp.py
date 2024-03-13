import pandas as pd 

df=pd.read_csv('gens.csv')

df['text']='Headline: '+df['sentence']+'. Belief based on the Headline: '+df['inference']
df.to_csv('gens3.csv')