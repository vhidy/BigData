
### Import Modul


```python
import numpy as np
import pandas as pd
```

### Series

```s = pd.Series(data, index=index)```
`data` dapat beberapa macam diataranya :
- sebuah Python dictionary
- sebuah ndarray
- sebuah nilai scalar (seperti 5)

##### data dari ndarray


```python
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s
```




    a    0.715224
    b    0.767742
    c   -0.291969
    d    0.798352
    e    1.117603
    dtype: float64




```python
s.index
```




    Index(['a', 'b', 'c', 'd', 'e'], dtype='object')




```python
pd.Series(np.random.randn(5))
```




    0   -1.091094
    1   -1.290440
    2   -0.475149
    3   -0.654700
    4   -1.127114
    dtype: float64



#### Data dari dictionary


```python
d = {'b' : 1, 'a' : 0, 'c' : 2}
pd.Series(d)
```




    b    1
    a    0
    c    2
    dtype: int64




```python
d = {'a' : 0., 'b' : 1., 'c' : 2.}
pd.Series(d)
```




    a    0.0
    b    1.0
    c    2.0
    dtype: float64




```python
pd.Series(d, index=['b', 'c', 'd', 'a'])
```




    b    1.0
    c    2.0
    d    NaN
    a    0.0
    dtype: float64



#### Data dari nilai scalar


```python
pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
```




    a    5.0
    b    5.0
    c    5.0
    d    5.0
    e    5.0
    dtype: float64



#### Series is ndarray-like


```python
s[0]
```




    0.7152237168723361




```python
s[:3]
```




    a    0.715224
    b    0.767742
    c   -0.291969
    dtype: float64




```python
s[s > s.median()]
```




    d    0.798352
    e    1.117603
    dtype: float64




```python
s[[4, 3, 1]]
```




    e    1.117603
    d    0.798352
    b    0.767742
    dtype: float64




```python
np.exp(s)
```




    a    2.044644
    b    2.154894
    c    0.746792
    d    2.221877
    e    3.057515
    dtype: float64



#### Series is dict-like


```python
s['a']
```




    0.7152237168723361




```python
s['e'] = 12.
s
```




    a     0.715224
    b     0.767742
    c    -0.291969
    d     0.798352
    e    12.000000
    dtype: float64




```python
'e' in s
```




    True




```python
'f' in s
```




    False



jika label tidak mengandung karakter yang dimaksud akan muncul error


```python
s['f']
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    ~/.local/lib/python3.7/site-packages/pandas/core/indexes/base.py in get_value(self, series, key)
       3123             try:
    -> 3124                 return libindex.get_value_box(s, key)
       3125             except IndexError:


    pandas/_libs/index.pyx in pandas._libs.index.get_value_box()


    pandas/_libs/index.pyx in pandas._libs.index.get_value_box()


    TypeError: 'str' object cannot be interpreted as an integer

    
    During handling of the above exception, another exception occurred:


    KeyError                                  Traceback (most recent call last)

    <ipython-input-19-c23937ec966b> in <module>()
    ----> 1 s['f']
    

    ~/.local/lib/python3.7/site-packages/pandas/core/series.py in __getitem__(self, key)
        765         key = com._apply_if_callable(key, self)
        766         try:
    --> 767             result = self.index.get_value(self, key)
        768 
        769             if not is_scalar(result):


    ~/.local/lib/python3.7/site-packages/pandas/core/indexes/base.py in get_value(self, series, key)
       3130                     raise InvalidIndexError(key)
       3131                 else:
    -> 3132                     raise e1
       3133             except Exception:  # pragma: no cover
       3134                 raise e1


    ~/.local/lib/python3.7/site-packages/pandas/core/indexes/base.py in get_value(self, series, key)
       3116         try:
       3117             return self._engine.get_value(s, k,
    -> 3118                                           tz=getattr(series.dtype, 'tz', None))
       3119         except KeyError as e1:
       3120             if len(self) > 0 and self.inferred_type in ['integer', 'boolean']:


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_value()


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_value()


    pandas/_libs/index.pyx in pandas._libs.index.IndexEngine.get_loc()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    pandas/_libs/hashtable_class_helper.pxi in pandas._libs.hashtable.PyObjectHashTable.get_item()


    KeyError: 'f'


jika tidak ingin mendapatkan error tapi digantikan dengan None maka bisa menggunakan method `get`


```python
s.get('f')
s.get('f', np.nan)
```




    nan



#### Operasi vektor pelabelan menggunakan series


```python
s + s
```




    a     1.430447
    b     1.535483
    c    -0.583937
    d     1.596704
    e    24.000000
    dtype: float64




```python
s * 2
```




    a     1.430447
    b     1.535483
    c    -0.583937
    d     1.596704
    e    24.000000
    dtype: float64




```python
np.exp(s)
```




    a         2.044644
    b         2.154894
    c         0.746792
    d         2.221877
    e    162754.791419
    dtype: float64




```python
s[1:] + s[:-1]
```




    a         NaN
    b    1.535483
    c   -0.583937
    d    1.596704
    e         NaN
    dtype: float64



#### Atribut Nama


```python
s = pd.Series(np.random.randn(5), name='something')
s
```




    0    0.001918
    1   -1.740851
    2    0.543277
    3    1.772499
    4    0.204512
    Name: something, dtype: float64




```python
s.name
```




    'something'



mengubah nama atribut series


```python
s2 = s.rename("different")
s2.name
```




    'different'



### DataFrame
DataFrame adalah struktur data berlabel 2 dimensi dengan kolom jenis yang berpotensi berbeda. Seperti series, DataFrame menerima berbagai macam input:

- Dict of 1D ndarrays, lists, dicts, or Series
- 2-D numpy.ndarray
- Structured or record ndarray
- Sebuah Series
- dari DataFrame yang lain

#### Data dari Dict series atau Dict


```python
d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(d, index=['d', 'b', 'a'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>two</th>
      <th>three</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>d</th>
      <td>4.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.index
```




    Index(['a', 'b', 'c', 'd'], dtype='object')




```python
df.columns
```




    Index(['one', 'two'], dtype='object')



#### Data dari Dict ndarrays / List


```python
d = {'one' : [1., 2., 3., 4.], 'two' : [4., 3., 2., 1.]}
```


```python
pd.DataFrame(d)
pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>d</th>
      <td>4.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



#### Data dari Record Array Terstruktur


```python
data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
data[:] = [(1,2.,'Hello'), (2,3.,"World")]
pd.DataFrame(data)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2.0</td>
      <td>b'Hello'</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3.0</td>
      <td>b'World'</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data, index=['first', 'second'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>first</th>
      <td>1</td>
      <td>2.0</td>
      <td>b'Hello'</td>
    </tr>
    <tr>
      <th>second</th>
      <td>2</td>
      <td>3.0</td>
      <td>b'World'</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data, columns=['C', 'A', 'B'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b'Hello'</td>
      <td>1</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b'World'</td>
      <td>2</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



#### Dari sebuah list dictionary


```python
data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
pd.DataFrame(data2)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>10</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data2, index=['first', 'second'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>first</th>
      <td>1</td>
      <td>2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>second</th>
      <td>5</td>
      <td>10</td>
      <td>20.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame(data2, columns=['a', 'b'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



#### Dari sebuah Dictionary Tuple


```python
pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
              ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
              ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
              ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
              ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="3" halign="left">a</th>
      <th colspan="2" halign="left">b</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>b</th>
      <th>a</th>
      <th>c</th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">A</th>
      <th>B</th>
      <td>1.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>8.0</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>C</th>
      <td>2.0</td>
      <td>3.0</td>
      <td>6.0</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>D</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>



#### Dari sebuah Series
Hasilnya akan menjadi DataFrame dengan indeks yang sama dengan Series input, dan dengan satu kolom yang namanya adalah nama asli dari Series (hanya jika tidak ada nama kolom lain yang disediakan).

#### Konstruktor Alternatif
`DataFrame.from_dict` mengambil dict daro beberapa dict atau dict dari sebuah array sequences dan mengembalikan DataFrame


```python
pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]))
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])]),
                       orient='index', columns=['one', 'two', 'three'])
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
      <th>three</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>A</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>B</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
</div>



`DataFrame.from_records` mengambil daftar tupel atau ndarray dengan dtype terstruktur.


```python
data
```




    array([(1, 2., b'Hello'), (2, 3., b'World')],
          dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])




```python
pd.DataFrame.from_records(data, index='C')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>C</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b'Hello'</th>
      <td>1</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>b'World'</th>
      <td>2</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



#### Pemilihan kolom, penambahan, penghapusan


```python
df['one']
```




    a    1.0
    b    2.0
    c    3.0
    d    NaN
    Name: one, dtype: float64




```python
df['three'] = df['one'] * df['two']
df['flag'] = df['one'] > 2
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>two</th>
      <th>three</th>
      <th>flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>9.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>4.0</td>
      <td>NaN</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



Kolom dapat dihapus atau di-pop seperti dengan cara:


```python
del df['two']
three = df.pop('three')
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>flag</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>False</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>True</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>



Ketika menggunakan nilai skalar itu secara alami akan disimpan untuk mengisi kolom:


```python
df['foo'] = 'bar'
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>flag</th>
      <th>foo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>False</td>
      <td>bar</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>False</td>
      <td>bar</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>True</td>
      <td>bar</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>False</td>
      <td>bar</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['one_trunc'] = df['one'][:2]
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>flag</th>
      <th>foo</th>
      <th>one_trunc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>False</td>
      <td>bar</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>False</td>
      <td>bar</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>True</td>
      <td>bar</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>False</td>
      <td>bar</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.insert(1, 'bar', df['one'])
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>one</th>
      <th>bar</th>
      <th>flag</th>
      <th>foo</th>
      <th>one_trunc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>False</td>
      <td>bar</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>2.0</td>
      <td>2.0</td>
      <td>False</td>
      <td>bar</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>True</td>
      <td>bar</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>d</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>bar</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



#### Indexing / Selection

| Operation                      | Syntax          | Result     |
|--------------------------------|-----------------|------------|
| Select column	                 | `df[col]`       | Series     |
| Select row by label            | `df.loc[label]` | Series     |
| Select row by integer location | `df.iloc[loc]`  | Series     |
| Slice rows                     | `df[5:10]`      | DataFrame  |
| Select rows by boolean vector  | `df[bool_vec]`  | DataFrame  |

Seleksi baris, misalnya, mengembalikan Series yang indeksnya adalah kolom dari DataFrame:


```python
df.loc['b']
```




    one              2
    bar              2
    flag         False
    foo            bar
    one_trunc        2
    Name: b, dtype: object




```python
df.iloc[2]
```




    one             3
    bar             3
    flag         True
    foo           bar
    one_trunc     NaN
    Name: c, dtype: object



#### Penjajaran Data dan Aritmatika


```python
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
df + df2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.640102</td>
      <td>-1.579391</td>
      <td>1.438475</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.528026</td>
      <td>2.029622</td>
      <td>1.305880</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.234257</td>
      <td>-0.205642</td>
      <td>-1.498467</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.065475</td>
      <td>-0.793135</td>
      <td>0.281450</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.891015</td>
      <td>-1.316124</td>
      <td>-0.722498</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-0.356689</td>
      <td>-0.818944</td>
      <td>0.338891</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.174099</td>
      <td>-1.276321</td>
      <td>-0.070123</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df - df.iloc[0]
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-1.773932</td>
      <td>1.230308</td>
      <td>-0.928119</td>
      <td>-0.730980</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.052575</td>
      <td>-1.411526</td>
      <td>-1.791710</td>
      <td>-0.123784</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.318154</td>
      <td>0.077537</td>
      <td>-0.230048</td>
      <td>1.063831</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-1.626764</td>
      <td>0.590126</td>
      <td>-1.445795</td>
      <td>0.433144</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-2.068756</td>
      <td>-0.434940</td>
      <td>-0.705870</td>
      <td>0.260809</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.707491</td>
      <td>-0.527350</td>
      <td>-1.390303</td>
      <td>-0.795887</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.354410</td>
      <td>-0.393860</td>
      <td>0.323880</td>
      <td>-1.552373</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-1.149997</td>
      <td>-0.029797</td>
      <td>0.007593</td>
      <td>0.496321</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-1.836038</td>
      <td>0.677921</td>
      <td>0.429839</td>
      <td>-0.229944</td>
    </tr>
  </tbody>
</table>
</div>




```python
index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=list('ABC'))
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>0.717362</td>
      <td>-0.473780</td>
      <td>0.726707</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>1.349179</td>
      <td>-0.934736</td>
      <td>0.808596</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>0.236053</td>
      <td>0.100838</td>
      <td>-1.815250</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>0.015168</td>
      <td>-0.103056</td>
      <td>-0.712370</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-0.080777</td>
      <td>1.614723</td>
      <td>0.180478</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-0.100040</td>
      <td>-0.152784</td>
      <td>0.616512</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-0.079604</td>
      <td>-0.171881</td>
      <td>0.045603</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>0.047679</td>
      <td>0.227655</td>
      <td>0.244437</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(df['A'])
```




    pandas.core.series.Series




```python
df - df['A']
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2000-01-01 00:00:00</th>
      <th>2000-01-02 00:00:00</th>
      <th>2000-01-03 00:00:00</th>
      <th>2000-01-04 00:00:00</th>
      <th>2000-01-05 00:00:00</th>
      <th>2000-01-06 00:00:00</th>
      <th>2000-01-07 00:00:00</th>
      <th>2000-01-08 00:00:00</th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>NaN</td>
      <td>NaN</td>
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
      <th>2000-01-02</th>
      <td>NaN</td>
      <td>NaN</td>
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
      <th>2000-01-03</th>
      <td>NaN</td>
      <td>NaN</td>
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
      <th>2000-01-04</th>
      <td>NaN</td>
      <td>NaN</td>
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
      <th>2000-01-05</th>
      <td>NaN</td>
      <td>NaN</td>
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
      <th>2000-01-06</th>
      <td>NaN</td>
      <td>NaN</td>
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
      <th>2000-01-07</th>
      <td>NaN</td>
      <td>NaN</td>
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
      <th>2000-01-08</th>
      <td>NaN</td>
      <td>NaN</td>
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
</div>



Operasi dengan skalar sama seperti biasanya:


```python
df * 5 + 2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>5.586809</td>
      <td>-0.368902</td>
      <td>5.633534</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>8.745897</td>
      <td>-2.673678</td>
      <td>6.042980</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>3.180263</td>
      <td>2.504188</td>
      <td>-7.076248</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>2.075841</td>
      <td>1.484719</td>
      <td>-1.561849</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>1.596116</td>
      <td>10.073616</td>
      <td>2.902391</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>1.499799</td>
      <td>1.236082</td>
      <td>5.082561</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>1.601979</td>
      <td>1.140596</td>
      <td>2.228017</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>2.238395</td>
      <td>3.138274</td>
      <td>3.222187</td>
    </tr>
  </tbody>
</table>
</div>




```python
1 / df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>1.393997</td>
      <td>-2.110683</td>
      <td>1.376071</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>0.741191</td>
      <td>-1.069821</td>
      <td>1.236711</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>4.236345</td>
      <td>9.916940</td>
      <td>-0.550888</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>65.927143</td>
      <td>-9.703452</td>
      <td>-1.403765</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>-12.379806</td>
      <td>0.619301</td>
      <td>5.540834</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>-9.995981</td>
      <td>-6.545201</td>
      <td>1.622028</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>-12.562138</td>
      <td>-5.817986</td>
      <td>21.928234</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>20.973586</td>
      <td>4.392615</td>
      <td>4.091027</td>
    </tr>
  </tbody>
</table>
</div>




```python
df ** 4
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2000-01-01</th>
      <td>2.648213e-01</td>
      <td>0.050386</td>
      <td>0.278893</td>
    </tr>
    <tr>
      <th>2000-01-02</th>
      <td>3.313437e+00</td>
      <td>0.763405</td>
      <td>0.427491</td>
    </tr>
    <tr>
      <th>2000-01-03</th>
      <td>3.104808e-03</td>
      <td>0.000103</td>
      <td>10.857887</td>
    </tr>
    <tr>
      <th>2000-01-04</th>
      <td>5.293501e-08</td>
      <td>0.000113</td>
      <td>0.257527</td>
    </tr>
    <tr>
      <th>2000-01-05</th>
      <td>4.257402e-05</td>
      <td>6.798176</td>
      <td>0.001061</td>
    </tr>
    <tr>
      <th>2000-01-06</th>
      <td>1.001609e-04</td>
      <td>0.000545</td>
      <td>0.144466</td>
    </tr>
    <tr>
      <th>2000-01-07</th>
      <td>4.015557e-05</td>
      <td>0.000873</td>
      <td>0.000004</td>
    </tr>
    <tr>
      <th>2000-01-08</th>
      <td>5.167842e-06</td>
      <td>0.002686</td>
      <td>0.003570</td>
    </tr>
  </tbody>
</table>
</div>



Operator Boolean juga berfungsi:


```python
df1 = pd.DataFrame({'a' : [1, 0, 1], 'b' : [0, 1, 1] }, dtype=bool)
df2 = pd.DataFrame({'a' : [0, 1, 1], 'b' : [1, 1, 0] }, dtype=bool)
df1 & df2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 | df2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>True</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1 ^ df2
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
-df1
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>False</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>


