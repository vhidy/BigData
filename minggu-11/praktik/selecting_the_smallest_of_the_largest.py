import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50


movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
print(movie2.head())
print(movie2.nlargest(100, 'imdb_score').head())
print(movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget'))
