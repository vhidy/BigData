import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50


movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
print(movie2.head())
print(movie2.nlargest(100, 'imdb_score').head())
print(movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget'))

movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'title_year', 'imdb_score']]
print(movie2.sort_values('title_year', ascending=False).head())

movie3 = movie2.sort_values(['title_year','imdb_score'], ascending=False)
print(movie3.head())

movie_top_year = movie3.drop_duplicates(subset='title_year')
print(movie_top_year.head())

movie4 = movie[['movie_title', 'title_year', 'content_rating', 'budget']]
movie4_sorted = movie4.sort_values(['title_year', 'content_rating', 'budget'], 
                                   ascending=[False, False, True])
movie4_sorted.drop_duplicates(subset=['title_year', 'content_rating']).head(10)
