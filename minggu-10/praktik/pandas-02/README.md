
# Chapter 2: Essential DataFrame Operations


```python
# Import Modul

import pandas as pd
import numpy as np
pd.options.display.max_columns = 40
```

# Menampilkan beberapa kolom pada DataFrame


```python
movie = pd.read_csv('data/movie.csv')
movie_actor_director = movie[['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name']]
movie_actor_director.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_1_name</th>
      <th>actor_2_name</th>
      <th>actor_3_name</th>
      <th>director_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CCH Pounder</td>
      <td>Joel David Moore</td>
      <td>Wes Studi</td>
      <td>James Cameron</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Johnny Depp</td>
      <td>Orlando Bloom</td>
      <td>Jack Davenport</td>
      <td>Gore Verbinski</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Christoph Waltz</td>
      <td>Rory Kinnear</td>
      <td>Stephanie Sigman</td>
      <td>Sam Mendes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tom Hardy</td>
      <td>Christian Bale</td>
      <td>Joseph Gordon-Levitt</td>
      <td>Christopher Nolan</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Doug Walker</td>
      <td>Rob Walker</td>
      <td>NaN</td>
      <td>Doug Walker</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie[['director_name']].head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>director_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>James Cameron</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Gore Verbinski</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sam Mendes</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Christopher Nolan</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Doug Walker</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name']
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
       2441             try:
    -> 2442                 return self._engine.get_loc(key)
       2443             except KeyError:


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc (pandas/_libs/index.c:5280)()


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc (pandas/_libs/index.c:5126)()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20523)()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20477)()


    KeyError: ('actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name')

    
    During handling of the above exception, another exception occurred:


    KeyError                                  Traceback (most recent call last)

    <ipython-input-4-954222273e42> in <module>()
    ----> 1 movie['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name']
    

    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/frame.py in __getitem__(self, key)
       1962             return self._getitem_multilevel(key)
       1963         else:
    -> 1964             return self._getitem_column(key)
       1965 
       1966     def _getitem_column(self, key):


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/frame.py in _getitem_column(self, key)
       1969         # get column
       1970         if self.columns.is_unique:
    -> 1971             return self._get_item_cache(key)
       1972 
       1973         # duplicate columns & possible reduce dimensionality


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/generic.py in _get_item_cache(self, item)
       1643         res = cache.get(item)
       1644         if res is None:
    -> 1645             values = self._data.get(item)
       1646             res = self._box_item_values(item, values)
       1647             cache[item] = res


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/internals.py in get(self, item, fastpath)
       3588 
       3589             if not isnull(item):
    -> 3590                 loc = self.items.get_loc(item)
       3591             else:
       3592                 indexer = np.arange(len(self.items))[isnull(self.items)]


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/indexes/base.py in get_loc(self, key, method, tolerance)
       2442                 return self._engine.get_loc(key)
       2443             except KeyError:
    -> 2444                 return self._engine.get_loc(self._maybe_cast_indexer(key))
       2445 
       2446         indexer = self.get_indexer([key], method=method, tolerance=tolerance)


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc (pandas/_libs/index.c:5280)()


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc (pandas/_libs/index.c:5126)()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20523)()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item (pandas/_libs/hashtable.c:20477)()


    KeyError: ('actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name')



```python
cols =['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name']
movie_actor_director = movie[cols]
```

# Menampilkan beberapa kolom dengan method


```python
movie = pd.read_csv('data/movie.csv', index_col='movie_title')
movie.get_dtype_counts()
```




    float64    13
    int64       3
    object     11
    dtype: int64




```python
movie.select_dtypes(include=['int']).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_voted_users</th>
      <th>cast_total_facebook_likes</th>
      <th>movie_facebook_likes</th>
    </tr>
    <tr>
      <th>movie_title</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avatar</th>
      <td>886204</td>
      <td>4834</td>
      <td>33000</td>
    </tr>
    <tr>
      <th>Pirates of the Caribbean: At World's End</th>
      <td>471220</td>
      <td>48350</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Spectre</th>
      <td>275868</td>
      <td>11700</td>
      <td>85000</td>
    </tr>
    <tr>
      <th>The Dark Knight Rises</th>
      <td>1144337</td>
      <td>106759</td>
      <td>164000</td>
    </tr>
    <tr>
      <th>Star Wars: Episode VII - The Force Awakens</th>
      <td>8</td>
      <td>143</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie.select_dtypes(include=['number']).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_critic_for_reviews</th>
      <th>duration</th>
      <th>director_facebook_likes</th>
      <th>actor_3_facebook_likes</th>
      <th>actor_1_facebook_likes</th>
      <th>gross</th>
      <th>num_voted_users</th>
      <th>cast_total_facebook_likes</th>
      <th>facenumber_in_poster</th>
      <th>num_user_for_reviews</th>
      <th>budget</th>
      <th>title_year</th>
      <th>actor_2_facebook_likes</th>
      <th>imdb_score</th>
      <th>aspect_ratio</th>
      <th>movie_facebook_likes</th>
    </tr>
    <tr>
      <th>movie_title</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avatar</th>
      <td>723.0</td>
      <td>178.0</td>
      <td>0.0</td>
      <td>855.0</td>
      <td>1000.0</td>
      <td>760505847.0</td>
      <td>886204</td>
      <td>4834</td>
      <td>0.0</td>
      <td>3054.0</td>
      <td>237000000.0</td>
      <td>2009.0</td>
      <td>936.0</td>
      <td>7.9</td>
      <td>1.78</td>
      <td>33000</td>
    </tr>
    <tr>
      <th>Pirates of the Caribbean: At World's End</th>
      <td>302.0</td>
      <td>169.0</td>
      <td>563.0</td>
      <td>1000.0</td>
      <td>40000.0</td>
      <td>309404152.0</td>
      <td>471220</td>
      <td>48350</td>
      <td>0.0</td>
      <td>1238.0</td>
      <td>300000000.0</td>
      <td>2007.0</td>
      <td>5000.0</td>
      <td>7.1</td>
      <td>2.35</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Spectre</th>
      <td>602.0</td>
      <td>148.0</td>
      <td>0.0</td>
      <td>161.0</td>
      <td>11000.0</td>
      <td>200074175.0</td>
      <td>275868</td>
      <td>11700</td>
      <td>1.0</td>
      <td>994.0</td>
      <td>245000000.0</td>
      <td>2015.0</td>
      <td>393.0</td>
      <td>6.8</td>
      <td>2.35</td>
      <td>85000</td>
    </tr>
    <tr>
      <th>The Dark Knight Rises</th>
      <td>813.0</td>
      <td>164.0</td>
      <td>22000.0</td>
      <td>23000.0</td>
      <td>27000.0</td>
      <td>448130642.0</td>
      <td>1144337</td>
      <td>106759</td>
      <td>0.0</td>
      <td>2701.0</td>
      <td>250000000.0</td>
      <td>2012.0</td>
      <td>23000.0</td>
      <td>8.5</td>
      <td>2.35</td>
      <td>164000</td>
    </tr>
    <tr>
      <th>Star Wars: Episode VII - The Force Awakens</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>131.0</td>
      <td>NaN</td>
      <td>131.0</td>
      <td>NaN</td>
      <td>8</td>
      <td>143</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12.0</td>
      <td>7.1</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie.filter(like='facebook').head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>director_facebook_likes</th>
      <th>actor_3_facebook_likes</th>
      <th>actor_1_facebook_likes</th>
      <th>cast_total_facebook_likes</th>
      <th>actor_2_facebook_likes</th>
      <th>movie_facebook_likes</th>
    </tr>
    <tr>
      <th>movie_title</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avatar</th>
      <td>0.0</td>
      <td>855.0</td>
      <td>1000.0</td>
      <td>4834</td>
      <td>936.0</td>
      <td>33000</td>
    </tr>
    <tr>
      <th>Pirates of the Caribbean: At World's End</th>
      <td>563.0</td>
      <td>1000.0</td>
      <td>40000.0</td>
      <td>48350</td>
      <td>5000.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Spectre</th>
      <td>0.0</td>
      <td>161.0</td>
      <td>11000.0</td>
      <td>11700</td>
      <td>393.0</td>
      <td>85000</td>
    </tr>
    <tr>
      <th>The Dark Knight Rises</th>
      <td>22000.0</td>
      <td>23000.0</td>
      <td>27000.0</td>
      <td>106759</td>
      <td>23000.0</td>
      <td>164000</td>
    </tr>
    <tr>
      <th>Star Wars: Episode VII - The Force Awakens</th>
      <td>131.0</td>
      <td>NaN</td>
      <td>131.0</td>
      <td>143</td>
      <td>12.0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie.filter(regex='\d').head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_3_facebook_likes</th>
      <th>actor_2_name</th>
      <th>actor_1_facebook_likes</th>
      <th>actor_1_name</th>
      <th>actor_3_name</th>
      <th>actor_2_facebook_likes</th>
    </tr>
    <tr>
      <th>movie_title</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avatar</th>
      <td>855.0</td>
      <td>Joel David Moore</td>
      <td>1000.0</td>
      <td>CCH Pounder</td>
      <td>Wes Studi</td>
      <td>936.0</td>
    </tr>
    <tr>
      <th>Pirates of the Caribbean: At World's End</th>
      <td>1000.0</td>
      <td>Orlando Bloom</td>
      <td>40000.0</td>
      <td>Johnny Depp</td>
      <td>Jack Davenport</td>
      <td>5000.0</td>
    </tr>
    <tr>
      <th>Spectre</th>
      <td>161.0</td>
      <td>Rory Kinnear</td>
      <td>11000.0</td>
      <td>Christoph Waltz</td>
      <td>Stephanie Sigman</td>
      <td>393.0</td>
    </tr>
    <tr>
      <th>The Dark Knight Rises</th>
      <td>23000.0</td>
      <td>Christian Bale</td>
      <td>27000.0</td>
      <td>Tom Hardy</td>
      <td>Joseph Gordon-Levitt</td>
      <td>23000.0</td>
    </tr>
    <tr>
      <th>Star Wars: Episode VII - The Force Awakens</th>
      <td>NaN</td>
      <td>Rob Walker</td>
      <td>131.0</td>
      <td>Doug Walker</td>
      <td>NaN</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie.filter(items=['actor_1_name', 'asdf']).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>actor_1_name</th>
    </tr>
    <tr>
      <th>movie_title</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Avatar</th>
      <td>CCH Pounder</td>
    </tr>
    <tr>
      <th>Pirates of the Caribbean: At World's End</th>
      <td>Johnny Depp</td>
    </tr>
    <tr>
      <th>Spectre</th>
      <td>Christoph Waltz</td>
    </tr>
    <tr>
      <th>The Dark Knight Rises</th>
      <td>Tom Hardy</td>
    </tr>
    <tr>
      <th>Star Wars: Episode VII - The Force Awakens</th>
      <td>Doug Walker</td>
    </tr>
  </tbody>
</table>
</div>



# Mengurutkan nama kolom secara pantas


```python
movie = pd.read_csv('data/movie.csv')
```


```python
movie.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>director_name</th>
      <th>num_critic_for_reviews</th>
      <th>duration</th>
      <th>director_facebook_likes</th>
      <th>actor_3_facebook_likes</th>
      <th>actor_2_name</th>
      <th>actor_1_facebook_likes</th>
      <th>gross</th>
      <th>genres</th>
      <th>actor_1_name</th>
      <th>movie_title</th>
      <th>num_voted_users</th>
      <th>cast_total_facebook_likes</th>
      <th>actor_3_name</th>
      <th>facenumber_in_poster</th>
      <th>plot_keywords</th>
      <th>movie_imdb_link</th>
      <th>num_user_for_reviews</th>
      <th>language</th>
      <th>country</th>
      <th>content_rating</th>
      <th>budget</th>
      <th>title_year</th>
      <th>actor_2_facebook_likes</th>
      <th>imdb_score</th>
      <th>aspect_ratio</th>
      <th>movie_facebook_likes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Color</td>
      <td>James Cameron</td>
      <td>723.0</td>
      <td>178.0</td>
      <td>0.0</td>
      <td>855.0</td>
      <td>Joel David Moore</td>
      <td>1000.0</td>
      <td>760505847.0</td>
      <td>Action|Adventure|Fantasy|Sci-Fi</td>
      <td>CCH Pounder</td>
      <td>Avatar</td>
      <td>886204</td>
      <td>4834</td>
      <td>Wes Studi</td>
      <td>0.0</td>
      <td>avatar|future|marine|native|paraplegic</td>
      <td>http://www.imdb.com/title/tt0499549/?ref_=fn_t...</td>
      <td>3054.0</td>
      <td>English</td>
      <td>USA</td>
      <td>PG-13</td>
      <td>237000000.0</td>
      <td>2009.0</td>
      <td>936.0</td>
      <td>7.9</td>
      <td>1.78</td>
      <td>33000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Color</td>
      <td>Gore Verbinski</td>
      <td>302.0</td>
      <td>169.0</td>
      <td>563.0</td>
      <td>1000.0</td>
      <td>Orlando Bloom</td>
      <td>40000.0</td>
      <td>309404152.0</td>
      <td>Action|Adventure|Fantasy</td>
      <td>Johnny Depp</td>
      <td>Pirates of the Caribbean: At World's End</td>
      <td>471220</td>
      <td>48350</td>
      <td>Jack Davenport</td>
      <td>0.0</td>
      <td>goddess|marriage ceremony|marriage proposal|pi...</td>
      <td>http://www.imdb.com/title/tt0449088/?ref_=fn_t...</td>
      <td>1238.0</td>
      <td>English</td>
      <td>USA</td>
      <td>PG-13</td>
      <td>300000000.0</td>
      <td>2007.0</td>
      <td>5000.0</td>
      <td>7.1</td>
      <td>2.35</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Color</td>
      <td>Sam Mendes</td>
      <td>602.0</td>
      <td>148.0</td>
      <td>0.0</td>
      <td>161.0</td>
      <td>Rory Kinnear</td>
      <td>11000.0</td>
      <td>200074175.0</td>
      <td>Action|Adventure|Thriller</td>
      <td>Christoph Waltz</td>
      <td>Spectre</td>
      <td>275868</td>
      <td>11700</td>
      <td>Stephanie Sigman</td>
      <td>1.0</td>
      <td>bomb|espionage|sequel|spy|terrorist</td>
      <td>http://www.imdb.com/title/tt2379713/?ref_=fn_t...</td>
      <td>994.0</td>
      <td>English</td>
      <td>UK</td>
      <td>PG-13</td>
      <td>245000000.0</td>
      <td>2015.0</td>
      <td>393.0</td>
      <td>6.8</td>
      <td>2.35</td>
      <td>85000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Color</td>
      <td>Christopher Nolan</td>
      <td>813.0</td>
      <td>164.0</td>
      <td>22000.0</td>
      <td>23000.0</td>
      <td>Christian Bale</td>
      <td>27000.0</td>
      <td>448130642.0</td>
      <td>Action|Thriller</td>
      <td>Tom Hardy</td>
      <td>The Dark Knight Rises</td>
      <td>1144337</td>
      <td>106759</td>
      <td>Joseph Gordon-Levitt</td>
      <td>0.0</td>
      <td>deception|imprisonment|lawlessness|police offi...</td>
      <td>http://www.imdb.com/title/tt1345836/?ref_=fn_t...</td>
      <td>2701.0</td>
      <td>English</td>
      <td>USA</td>
      <td>PG-13</td>
      <td>250000000.0</td>
      <td>2012.0</td>
      <td>23000.0</td>
      <td>8.5</td>
      <td>2.35</td>
      <td>164000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>Doug Walker</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>131.0</td>
      <td>NaN</td>
      <td>Rob Walker</td>
      <td>131.0</td>
      <td>NaN</td>
      <td>Documentary</td>
      <td>Doug Walker</td>
      <td>Star Wars: Episode VII - The Force Awakens</td>
      <td>8</td>
      <td>143</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>http://www.imdb.com/title/tt5289954/?ref_=fn_t...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12.0</td>
      <td>7.1</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie.columns
```




    Index(['color', 'director_name', 'num_critic_for_reviews', 'duration',
           'director_facebook_likes', 'actor_3_facebook_likes', 'actor_2_name',
           'actor_1_facebook_likes', 'gross', 'genres', 'actor_1_name',
           'movie_title', 'num_voted_users', 'cast_total_facebook_likes',
           'actor_3_name', 'facenumber_in_poster', 'plot_keywords',
           'movie_imdb_link', 'num_user_for_reviews', 'language', 'country',
           'content_rating', 'budget', 'title_year', 'actor_2_facebook_likes',
           'imdb_score', 'aspect_ratio', 'movie_facebook_likes'],
          dtype='object')




```python
disc_core = ['movie_title','title_year', 'content_rating','genres']
disc_people = ['director_name','actor_1_name', 'actor_2_name','actor_3_name']
disc_other = ['color','country','language','plot_keywords','movie_imdb_link']
cont_fb = ['director_facebook_likes','actor_1_facebook_likes','actor_2_facebook_likes',
           'actor_3_facebook_likes', 'cast_total_facebook_likes', 'movie_facebook_likes']
cont_finance = ['budget','gross']
cont_num_reviews = ['num_voted_users','num_user_for_reviews', 'num_critic_for_reviews']
cont_other = ['imdb_score','duration', 'aspect_ratio', 'facenumber_in_poster']
```


```python
new_col_order = disc_core + disc_people + disc_other + \
                    cont_fb + cont_finance + cont_num_reviews + cont_other
set(movie.columns) == set(new_col_order)
```




    True




```python
movie2 = movie[new_col_order]
movie2.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>movie_title</th>
      <th>title_year</th>
      <th>content_rating</th>
      <th>genres</th>
      <th>director_name</th>
      <th>actor_1_name</th>
      <th>actor_2_name</th>
      <th>actor_3_name</th>
      <th>color</th>
      <th>country</th>
      <th>language</th>
      <th>plot_keywords</th>
      <th>movie_imdb_link</th>
      <th>director_facebook_likes</th>
      <th>actor_1_facebook_likes</th>
      <th>actor_2_facebook_likes</th>
      <th>actor_3_facebook_likes</th>
      <th>cast_total_facebook_likes</th>
      <th>movie_facebook_likes</th>
      <th>budget</th>
      <th>gross</th>
      <th>num_voted_users</th>
      <th>num_user_for_reviews</th>
      <th>num_critic_for_reviews</th>
      <th>imdb_score</th>
      <th>duration</th>
      <th>aspect_ratio</th>
      <th>facenumber_in_poster</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Avatar</td>
      <td>2009.0</td>
      <td>PG-13</td>
      <td>Action|Adventure|Fantasy|Sci-Fi</td>
      <td>James Cameron</td>
      <td>CCH Pounder</td>
      <td>Joel David Moore</td>
      <td>Wes Studi</td>
      <td>Color</td>
      <td>USA</td>
      <td>English</td>
      <td>avatar|future|marine|native|paraplegic</td>
      <td>http://www.imdb.com/title/tt0499549/?ref_=fn_t...</td>
      <td>0.0</td>
      <td>1000.0</td>
      <td>936.0</td>
      <td>855.0</td>
      <td>4834</td>
      <td>33000</td>
      <td>237000000.0</td>
      <td>760505847.0</td>
      <td>886204</td>
      <td>3054.0</td>
      <td>723.0</td>
      <td>7.9</td>
      <td>178.0</td>
      <td>1.78</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pirates of the Caribbean: At World's End</td>
      <td>2007.0</td>
      <td>PG-13</td>
      <td>Action|Adventure|Fantasy</td>
      <td>Gore Verbinski</td>
      <td>Johnny Depp</td>
      <td>Orlando Bloom</td>
      <td>Jack Davenport</td>
      <td>Color</td>
      <td>USA</td>
      <td>English</td>
      <td>goddess|marriage ceremony|marriage proposal|pi...</td>
      <td>http://www.imdb.com/title/tt0449088/?ref_=fn_t...</td>
      <td>563.0</td>
      <td>40000.0</td>
      <td>5000.0</td>
      <td>1000.0</td>
      <td>48350</td>
      <td>0</td>
      <td>300000000.0</td>
      <td>309404152.0</td>
      <td>471220</td>
      <td>1238.0</td>
      <td>302.0</td>
      <td>7.1</td>
      <td>169.0</td>
      <td>2.35</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Spectre</td>
      <td>2015.0</td>
      <td>PG-13</td>
      <td>Action|Adventure|Thriller</td>
      <td>Sam Mendes</td>
      <td>Christoph Waltz</td>
      <td>Rory Kinnear</td>
      <td>Stephanie Sigman</td>
      <td>Color</td>
      <td>UK</td>
      <td>English</td>
      <td>bomb|espionage|sequel|spy|terrorist</td>
      <td>http://www.imdb.com/title/tt2379713/?ref_=fn_t...</td>
      <td>0.0</td>
      <td>11000.0</td>
      <td>393.0</td>
      <td>161.0</td>
      <td>11700</td>
      <td>85000</td>
      <td>245000000.0</td>
      <td>200074175.0</td>
      <td>275868</td>
      <td>994.0</td>
      <td>602.0</td>
      <td>6.8</td>
      <td>148.0</td>
      <td>2.35</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>The Dark Knight Rises</td>
      <td>2012.0</td>
      <td>PG-13</td>
      <td>Action|Thriller</td>
      <td>Christopher Nolan</td>
      <td>Tom Hardy</td>
      <td>Christian Bale</td>
      <td>Joseph Gordon-Levitt</td>
      <td>Color</td>
      <td>USA</td>
      <td>English</td>
      <td>deception|imprisonment|lawlessness|police offi...</td>
      <td>http://www.imdb.com/title/tt1345836/?ref_=fn_t...</td>
      <td>22000.0</td>
      <td>27000.0</td>
      <td>23000.0</td>
      <td>23000.0</td>
      <td>106759</td>
      <td>164000</td>
      <td>250000000.0</td>
      <td>448130642.0</td>
      <td>1144337</td>
      <td>2701.0</td>
      <td>813.0</td>
      <td>8.5</td>
      <td>164.0</td>
      <td>2.35</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Star Wars: Episode VII - The Force Awakens</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Documentary</td>
      <td>Doug Walker</td>
      <td>Doug Walker</td>
      <td>Rob Walker</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>http://www.imdb.com/title/tt5289954/?ref_=fn_t...</td>
      <td>131.0</td>
      <td>131.0</td>
      <td>12.0</td>
      <td>NaN</td>
      <td>143</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



# Mengoperasikan seluruh DataFrame


```python
pd.options.display.max_rows = 8
movie = pd.read_csv('data/movie.csv')
movie.shape
```




    (4916, 28)




```python
movie.size
```




    137648




```python
movie.ndim
```




    2




```python
len(movie)
```




    4916




```python
movie.count()
```




    color                     4897
    director_name             4814
    num_critic_for_reviews    4867
    duration                  4901
                              ... 
    actor_2_facebook_likes    4903
    imdb_score                4916
    aspect_ratio              4590
    movie_facebook_likes      4916
    Length: 28, dtype: int64




```python
movie.min()
```




    num_critic_for_reviews     1.00
    duration                   7.00
    director_facebook_likes    0.00
    actor_3_facebook_likes     0.00
                               ... 
    actor_2_facebook_likes     0.00
    imdb_score                 1.60
    aspect_ratio               1.18
    movie_facebook_likes       0.00
    Length: 16, dtype: float64




```python
movie.describe()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_critic_for_reviews</th>
      <th>duration</th>
      <th>director_facebook_likes</th>
      <th>actor_3_facebook_likes</th>
      <th>actor_1_facebook_likes</th>
      <th>gross</th>
      <th>num_voted_users</th>
      <th>cast_total_facebook_likes</th>
      <th>facenumber_in_poster</th>
      <th>num_user_for_reviews</th>
      <th>budget</th>
      <th>title_year</th>
      <th>actor_2_facebook_likes</th>
      <th>imdb_score</th>
      <th>aspect_ratio</th>
      <th>movie_facebook_likes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4867.000000</td>
      <td>4901.000000</td>
      <td>4814.000000</td>
      <td>4893.000000</td>
      <td>4909.000000</td>
      <td>4.054000e+03</td>
      <td>4.916000e+03</td>
      <td>4916.000000</td>
      <td>4903.000000</td>
      <td>4895.000000</td>
      <td>4.432000e+03</td>
      <td>4810.000000</td>
      <td>4903.000000</td>
      <td>4916.000000</td>
      <td>4590.000000</td>
      <td>4916.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>137.988905</td>
      <td>107.090798</td>
      <td>691.014541</td>
      <td>631.276313</td>
      <td>6494.488491</td>
      <td>4.764451e+07</td>
      <td>8.264492e+04</td>
      <td>9579.815907</td>
      <td>1.377320</td>
      <td>267.668846</td>
      <td>3.654749e+07</td>
      <td>2002.447609</td>
      <td>1621.923516</td>
      <td>6.437429</td>
      <td>2.222349</td>
      <td>7348.294142</td>
    </tr>
    <tr>
      <th>std</th>
      <td>120.239379</td>
      <td>25.286015</td>
      <td>2832.954125</td>
      <td>1625.874802</td>
      <td>15106.986884</td>
      <td>6.737255e+07</td>
      <td>1.383222e+05</td>
      <td>18164.316990</td>
      <td>2.023826</td>
      <td>372.934839</td>
      <td>1.002427e+08</td>
      <td>12.453977</td>
      <td>4011.299523</td>
      <td>1.127802</td>
      <td>1.402940</td>
      <td>19206.016458</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>7.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.620000e+02</td>
      <td>5.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.180000e+02</td>
      <td>1916.000000</td>
      <td>0.000000</td>
      <td>1.600000</td>
      <td>1.180000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>49.000000</td>
      <td>93.000000</td>
      <td>7.000000</td>
      <td>132.000000</td>
      <td>607.000000</td>
      <td>5.019656e+06</td>
      <td>8.361750e+03</td>
      <td>1394.750000</td>
      <td>0.000000</td>
      <td>64.000000</td>
      <td>6.000000e+06</td>
      <td>1999.000000</td>
      <td>277.000000</td>
      <td>5.800000</td>
      <td>1.850000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>108.000000</td>
      <td>103.000000</td>
      <td>48.000000</td>
      <td>366.000000</td>
      <td>982.000000</td>
      <td>2.504396e+07</td>
      <td>3.313250e+04</td>
      <td>3049.000000</td>
      <td>1.000000</td>
      <td>153.000000</td>
      <td>1.985000e+07</td>
      <td>2005.000000</td>
      <td>593.000000</td>
      <td>6.600000</td>
      <td>2.350000</td>
      <td>159.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>191.000000</td>
      <td>118.000000</td>
      <td>189.750000</td>
      <td>633.000000</td>
      <td>11000.000000</td>
      <td>6.110841e+07</td>
      <td>9.377275e+04</td>
      <td>13616.750000</td>
      <td>2.000000</td>
      <td>320.500000</td>
      <td>4.300000e+07</td>
      <td>2011.000000</td>
      <td>912.000000</td>
      <td>7.200000</td>
      <td>2.350000</td>
      <td>2000.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>813.000000</td>
      <td>511.000000</td>
      <td>23000.000000</td>
      <td>23000.000000</td>
      <td>640000.000000</td>
      <td>7.605058e+08</td>
      <td>1.689764e+06</td>
      <td>656730.000000</td>
      <td>43.000000</td>
      <td>5060.000000</td>
      <td>4.200000e+09</td>
      <td>2016.000000</td>
      <td>137000.000000</td>
      <td>9.500000</td>
      <td>16.000000</td>
      <td>349000.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.options.display.max_rows = 10
```


```python
movie.describe(percentiles=[.01, .3, .99])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_critic_for_reviews</th>
      <th>duration</th>
      <th>director_facebook_likes</th>
      <th>actor_3_facebook_likes</th>
      <th>actor_1_facebook_likes</th>
      <th>gross</th>
      <th>num_voted_users</th>
      <th>cast_total_facebook_likes</th>
      <th>facenumber_in_poster</th>
      <th>num_user_for_reviews</th>
      <th>budget</th>
      <th>title_year</th>
      <th>actor_2_facebook_likes</th>
      <th>imdb_score</th>
      <th>aspect_ratio</th>
      <th>movie_facebook_likes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>4867.000000</td>
      <td>4901.000000</td>
      <td>4814.000000</td>
      <td>4893.000000</td>
      <td>4909.000000</td>
      <td>4.054000e+03</td>
      <td>4.916000e+03</td>
      <td>4916.000000</td>
      <td>4903.000000</td>
      <td>4895.000000</td>
      <td>4.432000e+03</td>
      <td>4810.000000</td>
      <td>4903.000000</td>
      <td>4916.000000</td>
      <td>4590.000000</td>
      <td>4916.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>137.988905</td>
      <td>107.090798</td>
      <td>691.014541</td>
      <td>631.276313</td>
      <td>6494.488491</td>
      <td>4.764451e+07</td>
      <td>8.264492e+04</td>
      <td>9579.815907</td>
      <td>1.377320</td>
      <td>267.668846</td>
      <td>3.654749e+07</td>
      <td>2002.447609</td>
      <td>1621.923516</td>
      <td>6.437429</td>
      <td>2.222349</td>
      <td>7348.294142</td>
    </tr>
    <tr>
      <th>std</th>
      <td>120.239379</td>
      <td>25.286015</td>
      <td>2832.954125</td>
      <td>1625.874802</td>
      <td>15106.986884</td>
      <td>6.737255e+07</td>
      <td>1.383222e+05</td>
      <td>18164.316990</td>
      <td>2.023826</td>
      <td>372.934839</td>
      <td>1.002427e+08</td>
      <td>12.453977</td>
      <td>4011.299523</td>
      <td>1.127802</td>
      <td>1.402940</td>
      <td>19206.016458</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>7.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.620000e+02</td>
      <td>5.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
      <td>2.180000e+02</td>
      <td>1916.000000</td>
      <td>0.000000</td>
      <td>1.600000</td>
      <td>1.180000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1%</th>
      <td>2.000000</td>
      <td>43.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>6.080000</td>
      <td>8.474800e+03</td>
      <td>5.300000e+01</td>
      <td>6.000000</td>
      <td>0.000000</td>
      <td>1.940000</td>
      <td>6.000000e+04</td>
      <td>1951.000000</td>
      <td>0.000000</td>
      <td>3.100000</td>
      <td>1.330000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>30%</th>
      <td>60.000000</td>
      <td>95.000000</td>
      <td>11.000000</td>
      <td>176.000000</td>
      <td>694.000000</td>
      <td>7.914069e+06</td>
      <td>1.186450e+04</td>
      <td>1684.500000</td>
      <td>0.000000</td>
      <td>80.000000</td>
      <td>8.000000e+06</td>
      <td>2000.000000</td>
      <td>345.000000</td>
      <td>6.000000</td>
      <td>1.850000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>108.000000</td>
      <td>103.000000</td>
      <td>48.000000</td>
      <td>366.000000</td>
      <td>982.000000</td>
      <td>2.504396e+07</td>
      <td>3.313250e+04</td>
      <td>3049.000000</td>
      <td>1.000000</td>
      <td>153.000000</td>
      <td>1.985000e+07</td>
      <td>2005.000000</td>
      <td>593.000000</td>
      <td>6.600000</td>
      <td>2.350000</td>
      <td>159.000000</td>
    </tr>
    <tr>
      <th>99%</th>
      <td>546.680000</td>
      <td>189.000000</td>
      <td>16000.000000</td>
      <td>11000.000000</td>
      <td>44920.000000</td>
      <td>3.264128e+08</td>
      <td>6.815846e+05</td>
      <td>62413.900000</td>
      <td>8.000000</td>
      <td>1999.240000</td>
      <td>2.000000e+08</td>
      <td>2016.000000</td>
      <td>17000.000000</td>
      <td>8.500000</td>
      <td>4.000000</td>
      <td>93850.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>813.000000</td>
      <td>511.000000</td>
      <td>23000.000000</td>
      <td>23000.000000</td>
      <td>640000.000000</td>
      <td>7.605058e+08</td>
      <td>1.689764e+06</td>
      <td>656730.000000</td>
      <td>43.000000</td>
      <td>5060.000000</td>
      <td>4.200000e+09</td>
      <td>2016.000000</td>
      <td>137000.000000</td>
      <td>9.500000</td>
      <td>16.000000</td>
      <td>349000.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.options.display.max_rows = 8
```


```python
movie.isnull().sum()
```




    color                      19
    director_name             102
    num_critic_for_reviews     49
    duration                   15
                             ... 
    actor_2_facebook_likes     13
    imdb_score                  0
    aspect_ratio              326
    movie_facebook_likes        0
    Length: 28, dtype: int64




```python
movie.min(skipna=False)
```




    num_critic_for_reviews     NaN
    duration                   NaN
    director_facebook_likes    NaN
    actor_3_facebook_likes     NaN
                              ... 
    actor_2_facebook_likes     NaN
    imdb_score                 1.6
    aspect_ratio               NaN
    movie_facebook_likes       0.0
    Length: 16, dtype: float64



# Menghubungkan DataFrame


```python
movie = pd.read_csv('data/movie.csv')
movie.isnull().head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>color</th>
      <th>director_name</th>
      <th>num_critic_for_reviews</th>
      <th>duration</th>
      <th>director_facebook_likes</th>
      <th>actor_3_facebook_likes</th>
      <th>actor_2_name</th>
      <th>actor_1_facebook_likes</th>
      <th>gross</th>
      <th>genres</th>
      <th>actor_1_name</th>
      <th>movie_title</th>
      <th>num_voted_users</th>
      <th>cast_total_facebook_likes</th>
      <th>actor_3_name</th>
      <th>facenumber_in_poster</th>
      <th>plot_keywords</th>
      <th>movie_imdb_link</th>
      <th>num_user_for_reviews</th>
      <th>language</th>
      <th>country</th>
      <th>content_rating</th>
      <th>budget</th>
      <th>title_year</th>
      <th>actor_2_facebook_likes</th>
      <th>imdb_score</th>
      <th>aspect_ratio</th>
      <th>movie_facebook_likes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
movie.isnull().sum().head()
```




    color                       19
    director_name              102
    num_critic_for_reviews      49
    duration                    15
    director_facebook_likes    102
    dtype: int64




```python
movie.isnull().sum().sum()
```




    2654




```python
movie.isnull().any().any()
```




    True




```python
movie.isnull().get_dtype_counts()
```




    bool    28
    dtype: int64




```python
movie[['color', 'movie_title', 'color']].max()
```




    Series([], dtype: float64)




```python
movie.select_dtypes(['object']).fillna('').max()
```




    color                                                          Color
    director_name                                          Étienne Faure
    actor_2_name                                           Zubaida Sahar
    genres                                                       Western
                                             ...                        
    movie_imdb_link    http://www.imdb.com/title/tt5574490/?ref_=fn_t...
    language                                                        Zulu
    country                                                 West Germany
    content_rating                                                     X
    Length: 12, dtype: object



# Menggunakan operator pada DataFrame

### Load dataset


```python
college = pd.read_csv('data/college.csv')
college + 5
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/ops.py in na_op(x, y)
       1175             result = expressions.evaluate(op, str_rep, x, y,
    -> 1176                                           raise_on_error=True, **eval_kwargs)
       1177         except TypeError:


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/computation/expressions.py in evaluate(op, op_str, a, b, raise_on_error, use_numexpr, **eval_kwargs)
        210         return _evaluate(op, op_str, a, b, raise_on_error=raise_on_error,
    --> 211                          **eval_kwargs)
        212     return _evaluate_standard(op, op_str, a, b, raise_on_error=raise_on_error)


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/computation/expressions.py in _evaluate_numexpr(op, op_str, a, b, raise_on_error, truediv, reversed, **eval_kwargs)
        121     if result is None:
    --> 122         result = _evaluate_standard(op, op_str, a, b, raise_on_error)
        123 


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/computation/expressions.py in _evaluate_standard(op, op_str, a, b, raise_on_error, **eval_kwargs)
         63     with np.errstate(all='ignore'):
    ---> 64         return op(a, b)
         65 


    TypeError: must be str, not int

    
    During handling of the above exception, another exception occurred:


    TypeError                                 Traceback (most recent call last)

    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/internals.py in eval(self, func, other, raise_on_error, try_cast, mgr)
       1183             with np.errstate(all='ignore'):
    -> 1184                 result = get_result(other)
       1185 


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/internals.py in get_result(other)
       1152             else:
    -> 1153                 result = func(values, other)
       1154 


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/ops.py in na_op(x, y)
       1201                     with np.errstate(all='ignore'):
    -> 1202                         result[mask] = op(xrav, y)
       1203             else:


    TypeError: must be str, not int

    
    During handling of the above exception, another exception occurred:


    TypeError                                 Traceback (most recent call last)

    <ipython-input-37-4749f68a2501> in <module>()
          1 college = pd.read_csv('data/college.csv')
    ----> 2 college + 5
    

    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/ops.py in f(self, other, axis, level, fill_value)
       1239                 self = self.fillna(fill_value)
       1240 
    -> 1241             return self._combine_const(other, na_op)
       1242 
       1243     f.__name__ = name


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/frame.py in _combine_const(self, other, func, raise_on_error)
       3541     def _combine_const(self, other, func, raise_on_error=True):
       3542         new_data = self._data.eval(func=func, other=other,
    -> 3543                                    raise_on_error=raise_on_error)
       3544         return self._constructor(new_data)
       3545 


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/internals.py in eval(self, **kwargs)
       3195 
       3196     def eval(self, **kwargs):
    -> 3197         return self.apply('eval', **kwargs)
       3198 
       3199     def quantile(self, **kwargs):


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/internals.py in apply(self, f, axes, filter, do_integrity_check, consolidate, **kwargs)
       3089 
       3090             kwargs['mgr'] = self
    -> 3091             applied = getattr(b, f)(**kwargs)
       3092             result_blocks = _extend_blocks(applied, result_blocks)
       3093 


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/internals.py in eval(self, func, other, raise_on_error, try_cast, mgr)
       1189             raise
       1190         except Exception as detail:
    -> 1191             result = handle_error()
       1192 
       1193         # technically a broadcast error in numpy can 'work' by returning a


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/internals.py in handle_error()
       1172                 # The 'detail' variable is defined in outer scope.
       1173                 raise TypeError('Could not operate %s with block values %s' %
    -> 1174                                 (repr(other), str(detail)))  # noqa
       1175             else:
       1176                 # return the values


    TypeError: Could not operate 5 with block values must be str, not int



```python
college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')
```


```python
college == 'asdf'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-39-697c8af60bcf> in <module>()
    ----> 1 college == 'asdf'
    

    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/ops.py in f(self, other)
       1302             # straight boolean comparisions we want to allow all columns
       1303             # (regardless of dtype to pass thru) See #4537 for discussion.
    -> 1304             res = self._combine_const(other, func, raise_on_error=False)
       1305             return res.fillna(True).astype(bool)
       1306 


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/frame.py in _combine_const(self, other, func, raise_on_error)
       3541     def _combine_const(self, other, func, raise_on_error=True):
       3542         new_data = self._data.eval(func=func, other=other,
    -> 3543                                    raise_on_error=raise_on_error)
       3544         return self._constructor(new_data)
       3545 


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/internals.py in eval(self, **kwargs)
       3195 
       3196     def eval(self, **kwargs):
    -> 3197         return self.apply('eval', **kwargs)
       3198 
       3199     def quantile(self, **kwargs):


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/internals.py in apply(self, f, axes, filter, do_integrity_check, consolidate, **kwargs)
       3089 
       3090             kwargs['mgr'] = self
    -> 3091             applied = getattr(b, f)(**kwargs)
       3092             result_blocks = _extend_blocks(applied, result_blocks)
       3093 


    /Users/Ted/anaconda/lib/python3.6/site-packages/pandas/core/internals.py in eval(self, func, other, raise_on_error, try_cast, mgr)
       1203 
       1204                 raise TypeError('Could not compare [%s] with block values' %
    -> 1205                                 repr(other))
       1206 
       1207         # transpose if needed


    TypeError: Could not compare ['asdf'] with block values



```python
college_ugds_.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>0.0333</td>
      <td>0.9353</td>
      <td>0.0055</td>
      <td>0.0019</td>
      <td>0.0024</td>
      <td>0.0019</td>
      <td>0.0000</td>
      <td>0.0059</td>
      <td>0.0138</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.5922</td>
      <td>0.2600</td>
      <td>0.0283</td>
      <td>0.0518</td>
      <td>0.0022</td>
      <td>0.0007</td>
      <td>0.0368</td>
      <td>0.0179</td>
      <td>0.0100</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.2990</td>
      <td>0.4192</td>
      <td>0.0069</td>
      <td>0.0034</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.2715</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.6988</td>
      <td>0.1255</td>
      <td>0.0382</td>
      <td>0.0376</td>
      <td>0.0143</td>
      <td>0.0002</td>
      <td>0.0172</td>
      <td>0.0332</td>
      <td>0.0350</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.0158</td>
      <td>0.9208</td>
      <td>0.0121</td>
      <td>0.0019</td>
      <td>0.0010</td>
      <td>0.0006</td>
      <td>0.0098</td>
      <td>0.0243</td>
      <td>0.0137</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_ugds_.head() + .00501
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>0.03831</td>
      <td>0.94031</td>
      <td>0.01051</td>
      <td>0.00691</td>
      <td>0.00741</td>
      <td>0.00691</td>
      <td>0.00501</td>
      <td>0.01091</td>
      <td>0.01881</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.59721</td>
      <td>0.26501</td>
      <td>0.03331</td>
      <td>0.05681</td>
      <td>0.00721</td>
      <td>0.00571</td>
      <td>0.04181</td>
      <td>0.02291</td>
      <td>0.01501</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.30401</td>
      <td>0.42421</td>
      <td>0.01191</td>
      <td>0.00841</td>
      <td>0.00501</td>
      <td>0.00501</td>
      <td>0.00501</td>
      <td>0.00501</td>
      <td>0.27651</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.70381</td>
      <td>0.13051</td>
      <td>0.04321</td>
      <td>0.04261</td>
      <td>0.01931</td>
      <td>0.00521</td>
      <td>0.02221</td>
      <td>0.03821</td>
      <td>0.04001</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.02081</td>
      <td>0.92581</td>
      <td>0.01711</td>
      <td>0.00691</td>
      <td>0.00601</td>
      <td>0.00561</td>
      <td>0.01481</td>
      <td>0.02931</td>
      <td>0.01871</td>
    </tr>
  </tbody>
</table>
</div>




```python
(college_ugds_.head() + .00501) // .01
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>3.0</td>
      <td>94.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>59.0</td>
      <td>26.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>30.0</td>
      <td>42.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>27.0</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>70.0</td>
      <td>13.0</td>
      <td>4.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>2.0</td>
      <td>92.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_ugds_op_round = (college_ugds_ + .00501) // .01 / 100
college_ugds_op_round.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>0.03</td>
      <td>0.94</td>
      <td>0.01</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.01</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.59</td>
      <td>0.26</td>
      <td>0.03</td>
      <td>0.05</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.04</td>
      <td>0.02</td>
      <td>0.01</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.30</td>
      <td>0.42</td>
      <td>0.01</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.27</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.70</td>
      <td>0.13</td>
      <td>0.04</td>
      <td>0.04</td>
      <td>0.01</td>
      <td>0.0</td>
      <td>0.02</td>
      <td>0.03</td>
      <td>0.04</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.02</td>
      <td>0.92</td>
      <td>0.01</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.01</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_ugds_round = (college_ugds_ + .00001).round(2)
college_ugds_round.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>0.03</td>
      <td>0.94</td>
      <td>0.01</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.01</td>
      <td>0.01</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.59</td>
      <td>0.26</td>
      <td>0.03</td>
      <td>0.05</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.04</td>
      <td>0.02</td>
      <td>0.01</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.30</td>
      <td>0.42</td>
      <td>0.01</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.27</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.70</td>
      <td>0.13</td>
      <td>0.04</td>
      <td>0.04</td>
      <td>0.01</td>
      <td>0.0</td>
      <td>0.02</td>
      <td>0.03</td>
      <td>0.04</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.02</td>
      <td>0.92</td>
      <td>0.01</td>
      <td>0.00</td>
      <td>0.00</td>
      <td>0.0</td>
      <td>0.01</td>
      <td>0.02</td>
      <td>0.01</td>
    </tr>
  </tbody>
</table>
</div>




```python
.045 + .005
```




    0.049999999999999996




```python
college_ugds_op_round.equals(college_ugds_round)
```




    True




```python
college_ugds_op_round_methods = college_ugds_.add(.00501).floordiv(.01).div(100)
```

# Membandingkan missing values


```python
np.nan == np.nan
```




    False




```python
None == None
```




    True




```python
5 > np.nan
```




    False




```python
np.nan > 5
```




    False




```python
5 != np.nan
```




    True




```python
college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')
```


```python
college_ugds_.head() == .0019
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_self_compare = college_ugds_ == college_ugds_
college_self_compare.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_self_compare.all()
```




    UGDS_WHITE    False
    UGDS_BLACK    False
    UGDS_HISP     False
    UGDS_ASIAN    False
                  ...  
    UGDS_NHPI     False
    UGDS_2MOR     False
    UGDS_NRA      False
    UGDS_UNKN     False
    Length: 9, dtype: bool




```python
(college_ugds_ == np.nan).sum()
```




    UGDS_WHITE    0
    UGDS_BLACK    0
    UGDS_HISP     0
    UGDS_ASIAN    0
                 ..
    UGDS_NHPI     0
    UGDS_2MOR     0
    UGDS_NRA      0
    UGDS_UNKN     0
    Length: 9, dtype: int64




```python
college_ugds_.isnull().sum()
```




    UGDS_WHITE    661
    UGDS_BLACK    661
    UGDS_HISP     661
    UGDS_ASIAN    661
                 ... 
    UGDS_NHPI     661
    UGDS_2MOR     661
    UGDS_NRA      661
    UGDS_UNKN     661
    Length: 9, dtype: int64




```python
from pandas.testing import assert_frame_equal
```


```python
assert_frame_equal(college_ugds_, college_ugds_)
```


```python
college_ugds_.eq(.0019).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



# Mengubah DataFrame


```python
college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')
college_ugds_.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>0.0333</td>
      <td>0.9353</td>
      <td>0.0055</td>
      <td>0.0019</td>
      <td>0.0024</td>
      <td>0.0019</td>
      <td>0.0000</td>
      <td>0.0059</td>
      <td>0.0138</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.5922</td>
      <td>0.2600</td>
      <td>0.0283</td>
      <td>0.0518</td>
      <td>0.0022</td>
      <td>0.0007</td>
      <td>0.0368</td>
      <td>0.0179</td>
      <td>0.0100</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.2990</td>
      <td>0.4192</td>
      <td>0.0069</td>
      <td>0.0034</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.2715</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.6988</td>
      <td>0.1255</td>
      <td>0.0382</td>
      <td>0.0376</td>
      <td>0.0143</td>
      <td>0.0002</td>
      <td>0.0172</td>
      <td>0.0332</td>
      <td>0.0350</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.0158</td>
      <td>0.9208</td>
      <td>0.0121</td>
      <td>0.0019</td>
      <td>0.0010</td>
      <td>0.0006</td>
      <td>0.0098</td>
      <td>0.0243</td>
      <td>0.0137</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_ugds_.count()
```




    UGDS_WHITE    6874
    UGDS_BLACK    6874
    UGDS_HISP     6874
    UGDS_ASIAN    6874
                  ... 
    UGDS_NHPI     6874
    UGDS_2MOR     6874
    UGDS_NRA      6874
    UGDS_UNKN     6874
    Length: 9, dtype: int64




```python
college_ugds_.count(axis=0)
```




    UGDS_WHITE    6874
    UGDS_BLACK    6874
    UGDS_HISP     6874
    UGDS_ASIAN    6874
                  ... 
    UGDS_NHPI     6874
    UGDS_2MOR     6874
    UGDS_NRA      6874
    UGDS_UNKN     6874
    Length: 9, dtype: int64




```python
college_ugds_.count(axis='index')
```




    UGDS_WHITE    6874
    UGDS_BLACK    6874
    UGDS_HISP     6874
    UGDS_ASIAN    6874
                  ... 
    UGDS_NHPI     6874
    UGDS_2MOR     6874
    UGDS_NRA      6874
    UGDS_UNKN     6874
    Length: 9, dtype: int64




```python
college_ugds_.count(axis='columns').head()
```




    INSTNM
    Alabama A & M University               9
    University of Alabama at Birmingham    9
    Amridge University                     9
    University of Alabama in Huntsville    9
    Alabama State University               9
    dtype: int64




```python
college_ugds_.sum(axis='columns').head()
```




    INSTNM
    Alabama A & M University               1.0000
    University of Alabama at Birmingham    0.9999
    Amridge University                     1.0000
    University of Alabama in Huntsville    1.0000
    Alabama State University               1.0000
    dtype: float64




```python
college_ugds_.median(axis='index')
```




    UGDS_WHITE    0.55570
    UGDS_BLACK    0.10005
    UGDS_HISP     0.07140
    UGDS_ASIAN    0.01290
                   ...   
    UGDS_NHPI     0.00000
    UGDS_2MOR     0.01750
    UGDS_NRA      0.00000
    UGDS_UNKN     0.01430
    Length: 9, dtype: float64




```python
college_ugds_cumsum = college_ugds_.cumsum(axis=1)
college_ugds_cumsum.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>0.0333</td>
      <td>0.9686</td>
      <td>0.9741</td>
      <td>0.9760</td>
      <td>0.9784</td>
      <td>0.9803</td>
      <td>0.9803</td>
      <td>0.9862</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.5922</td>
      <td>0.8522</td>
      <td>0.8805</td>
      <td>0.9323</td>
      <td>0.9345</td>
      <td>0.9352</td>
      <td>0.9720</td>
      <td>0.9899</td>
      <td>0.9999</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.2990</td>
      <td>0.7182</td>
      <td>0.7251</td>
      <td>0.7285</td>
      <td>0.7285</td>
      <td>0.7285</td>
      <td>0.7285</td>
      <td>0.7285</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.6988</td>
      <td>0.8243</td>
      <td>0.8625</td>
      <td>0.9001</td>
      <td>0.9144</td>
      <td>0.9146</td>
      <td>0.9318</td>
      <td>0.9650</td>
      <td>1.0000</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.0158</td>
      <td>0.9366</td>
      <td>0.9487</td>
      <td>0.9506</td>
      <td>0.9516</td>
      <td>0.9522</td>
      <td>0.9620</td>
      <td>0.9863</td>
      <td>1.0000</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_ugds_cumsum.sort_values('UGDS_HISP', ascending=False)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>New Beginning College of Cosmetology</th>
      <td>0.8957</td>
      <td>0.9305</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Virginia University of Lynchburg</th>
      <td>0.0120</td>
      <td>0.9921</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>Turning Point Beauty College</th>
      <td>0.1915</td>
      <td>0.2341</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>First Coast Barber Academy</th>
      <td>0.1667</td>
      <td>0.9445</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
      <td>1.0001</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Rasmussen College - Overland Park</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>National Personal Training Institute of Cleveland</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Bay Area Medical Academy - San Jose Satellite Location</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Excel Learning Center-San Antonio South</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>7535 rows × 9 columns</p>
</div>



# Menentukan keragaman kampus kampus


```python
pd.read_csv('data/college_diversity.csv', index_col='School')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Diversity Index</th>
    </tr>
    <tr>
      <th>School</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Rutgers University--Newark  Newark, NJ</th>
      <td>0.76</td>
    </tr>
    <tr>
      <th>Andrews University  Berrien Springs, MI</th>
      <td>0.74</td>
    </tr>
    <tr>
      <th>Stanford University  Stanford, CA</th>
      <td>0.74</td>
    </tr>
    <tr>
      <th>University of Houston  Houston, TX</th>
      <td>0.74</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>San Francisco State University  San Francisco, CA</th>
      <td>0.73</td>
    </tr>
    <tr>
      <th>University of Illinois--Chicago  Chicago, IL</th>
      <td>0.73</td>
    </tr>
    <tr>
      <th>New Jersey Institute of Technology  Newark, NJ</th>
      <td>0.72</td>
    </tr>
    <tr>
      <th>Texas Woman's University  Denton, TX</th>
      <td>0.72</td>
    </tr>
  </tbody>
</table>
<p>10 rows × 1 columns</p>
</div>




```python
college = pd.read_csv('data/college.csv', index_col='INSTNM')
college_ugds_ = college.filter(like='UGDS_')
college_ugds_.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>0.0333</td>
      <td>0.9353</td>
      <td>0.0055</td>
      <td>0.0019</td>
      <td>0.0024</td>
      <td>0.0019</td>
      <td>0.0000</td>
      <td>0.0059</td>
      <td>0.0138</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>0.5922</td>
      <td>0.2600</td>
      <td>0.0283</td>
      <td>0.0518</td>
      <td>0.0022</td>
      <td>0.0007</td>
      <td>0.0368</td>
      <td>0.0179</td>
      <td>0.0100</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>0.2990</td>
      <td>0.4192</td>
      <td>0.0069</td>
      <td>0.0034</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.0000</td>
      <td>0.2715</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>0.6988</td>
      <td>0.1255</td>
      <td>0.0382</td>
      <td>0.0376</td>
      <td>0.0143</td>
      <td>0.0002</td>
      <td>0.0172</td>
      <td>0.0332</td>
      <td>0.0350</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>0.0158</td>
      <td>0.9208</td>
      <td>0.0121</td>
      <td>0.0019</td>
      <td>0.0010</td>
      <td>0.0006</td>
      <td>0.0098</td>
      <td>0.0243</td>
      <td>0.0137</td>
    </tr>
  </tbody>
</table>
</div>




```python
college_ugds_.isnull().sum(axis=1).sort_values(ascending=False).head()
```




    INSTNM
    Excel Learning Center-San Antonio South         9
    Philadelphia College of Osteopathic Medicine    9
    Assemblies of God Theological Seminary          9
    Episcopal Divinity School                       9
    Phillips Graduate Institute                     9
    dtype: int64




```python
college_ugds_ = college_ugds_.dropna(how='all')
```


```python
college_ugds_.isnull().sum()
```




    UGDS_WHITE    0
    UGDS_BLACK    0
    UGDS_HISP     0
    UGDS_ASIAN    0
                 ..
    UGDS_NHPI     0
    UGDS_2MOR     0
    UGDS_NRA      0
    UGDS_UNKN     0
    Length: 9, dtype: int64




```python
college_ugds_.ge(.15).head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alabama A &amp; M University</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>University of Alabama at Birmingham</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Amridge University</th>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>University of Alabama in Huntsville</th>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>Alabama State University</th>
      <td>False</td>
      <td>True</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
diversity_metric = college_ugds_.ge(.15).sum(axis='columns')
diversity_metric.head()
```




    INSTNM
    Alabama A & M University               1
    University of Alabama at Birmingham    2
    Amridge University                     3
    University of Alabama in Huntsville    1
    Alabama State University               1
    dtype: int64




```python
diversity_metric.value_counts()
```




    1    3042
    2    2884
    3     876
    4      63
    0       7
    5       2
    dtype: int64




```python
diversity_metric.sort_values(ascending=False).head()
```




    INSTNM
    Regency Beauty Institute-Austin          5
    Central Texas Beauty College-Temple      5
    Sullivan and Cogliano Training Center    4
    Ambria College of Nursing                4
    Berkeley College-New York                4
    dtype: int64




```python
college_ugds_.loc[['Regency Beauty Institute-Austin', 
                          'Central Texas Beauty College-Temple']]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>UGDS_WHITE</th>
      <th>UGDS_BLACK</th>
      <th>UGDS_HISP</th>
      <th>UGDS_ASIAN</th>
      <th>UGDS_AIAN</th>
      <th>UGDS_NHPI</th>
      <th>UGDS_2MOR</th>
      <th>UGDS_NRA</th>
      <th>UGDS_UNKN</th>
    </tr>
    <tr>
      <th>INSTNM</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Regency Beauty Institute-Austin</th>
      <td>0.1867</td>
      <td>0.2133</td>
      <td>0.1600</td>
      <td>0.0000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.1733</td>
      <td>0.0</td>
      <td>0.2667</td>
    </tr>
    <tr>
      <th>Central Texas Beauty College-Temple</th>
      <td>0.1616</td>
      <td>0.2323</td>
      <td>0.2626</td>
      <td>0.0202</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.1717</td>
      <td>0.0</td>
      <td>0.1515</td>
    </tr>
  </tbody>
</table>
</div>




```python
us_news_top = ['Rutgers University-Newark', 
               'Andrews University', 
               'Stanford University', 
               'University of Houston',
               'University of Nevada-Las Vegas']
```


```python
diversity_metric.loc[us_news_top]
```




    INSTNM
    Rutgers University-Newark         4
    Andrews University                3
    Stanford University               3
    University of Houston             3
    University of Nevada-Las Vegas    3
    dtype: int64




```python
college_ugds_.max(axis=1).sort_values(ascending=False).head(10)
```




    INSTNM
    Dewey University-Manati                               1.0
    Yeshiva and Kollel Harbotzas Torah                    1.0
    Mr Leon's School of Hair Design-Lewiston              1.0
    Dewey University-Bayamon                              1.0
                                                         ... 
    Monteclaro Escuela de Hoteleria y Artes Culinarias    1.0
    Yeshiva Shaar Hatorah                                 1.0
    Bais Medrash Elyon                                    1.0
    Yeshiva of Nitra Rabbinical College                   1.0
    Length: 10, dtype: float64




```python
college_ugds_.loc['Talmudical Seminary Oholei Torah']
```




    UGDS_WHITE    1.0
    UGDS_BLACK    0.0
    UGDS_HISP     0.0
    UGDS_ASIAN    0.0
                 ... 
    UGDS_NHPI     0.0
    UGDS_2MOR     0.0
    UGDS_NRA      0.0
    UGDS_UNKN     0.0
    Name: Talmudical Seminary Oholei Torah, Length: 9, dtype: float64




```python
(college_ugds_ > .01).all(axis=1).any()
```




    True


