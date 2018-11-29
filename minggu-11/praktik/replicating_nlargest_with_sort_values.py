import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50


movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
movie_smallest_largest = movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget')
print(movie_smallest_largest)
print(movie2.sort_values('imdb_score', ascending=False).head(100).head())
print(movie2.sort_values('imdb_score', ascending=False).head(100).sort_values('budget').head())
print(movie2.nlargest(100, 'imdb_score').tail())
print(movie2.sort_values('imdb_score', ascending=False).head(100).tail())
