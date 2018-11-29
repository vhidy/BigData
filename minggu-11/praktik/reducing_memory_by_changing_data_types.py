import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50


college = pd.read_csv('./data/college.csv')
different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']
col2 = college.loc[:, different_cols]

print(col2.head())
print(col2.dtypes)

original_mem = col2.memory_usage(deep=True)
print(original_mem)

col2['RELAFFIL'] = col2['RELAFFIL'].astype(np.int8)
print(col2.dtypes)

col2.select_dtypes(include=['object']).nunique()
col2['STABBR'] = col2['STABBR'].astype('category')
print(col2.dtypes)

new_mem = col2.memory_usage(deep=True)
print(new_mem)
print(new_mem / original_mem)

college = pd.read_csv('data/college.csv')
college[['CURROPER', 'INSTNM']].memory_usage(deep=True)
college.loc[0, 'CURROPER'] = 10000000
college.loc[0, 'INSTNM'] = college.loc[0, 'INSTNM'] + 'a'
# college.loc[1, 'INSTNM'] = college.loc[1, 'INSTNM'] + 'a'
college[['CURROPER', 'INSTNM']].memory_usage(deep=True)

print(college['MENONLY'].dtype)
college['MENONLY'].astype('int8') # ValueError: Cannot convert non-finite values (NA or inf) to integer
print(college.describe(include=['int64', 'float64']).T)
print(college.describe(include=[np.int64, np.float64]).T)
college['RELAFFIL'] = college['RELAFFIL'].astype(np.int8)
print(college.describe(include=['int', 'float']).T)  # defaults to 64 bit int/floats
print(college.describe(include=['number']).T)  # also works as the default int/float are 64 bits

college['MENONLY'] = college['MENONLY'].astype('float16')
college['RELAFFIL'] = college['RELAFFIL'].astype('int8')
college.index = pd.Int64Index(college.index)
print(college.index.memory_usage())

movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
print(movie2.head())

print(movie2.nlargest(100, 'imdb_score').head())
print(movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget'))
