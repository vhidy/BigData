# 10 Minutes to Pandas

Impor modul modul yang dibutuhkan


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## Pembuatan Objek
Membuat Series dengan memberikan daftar nilai, membiarkan pandas membuat indeks bilangan bulat default:


```python
s = pd.Series([1,3,5,np.nan,6,8])
s
```




    0    1.0
    1    3.0
    2    5.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64



Membuat DataFrame dengan melewatkan array NumPy, dengan indeks datetime dan kolom berlabel:


```python
dates = pd.date_range('20130101', periods=6)
dates

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <th>2013-01-01</th>
      <td>0.755035</td>
      <td>-0.484612</td>
      <td>-0.717522</td>
      <td>-0.687850</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.257250</td>
      <td>-0.765153</td>
      <td>1.093545</td>
      <td>0.420117</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.922617</td>
      <td>2.047103</td>
      <td>-2.533124</td>
      <td>0.690853</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>0.355054</td>
      <td>0.300695</td>
      <td>-0.926397</td>
      <td>1.703721</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.759857</td>
      <td>0.366894</td>
      <td>-1.023559</td>
      <td>0.070350</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>-1.370062</td>
      <td>1.064458</td>
      <td>0.188206</td>
      <td>-0.977349</td>
    </tr>
  </tbody>
</table>
</div>



Membuat DataFrame dengan melewatkan sebuah objek yang dapat dikonversi menjadi series-like.


```python
df2 = pd.DataFrame({ 'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

df2
df2.dtypes
```




    A           float64
    B    datetime64[ns]
    C           float32
    D             int32
    E          category
    F            object
    dtype: object



## Menampilkan Data
Berikut ini cara melihat baris atas dan bawah frame:


```python
df.head()
df.tail(3)
df.index
df.columns
df.values
df.describe()
df.T
df.sort_index(axis=1, ascending=False)
df.sort_values(by='B')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <th>2013-01-02</th>
      <td>-0.257250</td>
      <td>-0.765153</td>
      <td>1.093545</td>
      <td>0.420117</td>
    </tr>
    <tr>
      <th>2013-01-01</th>
      <td>0.755035</td>
      <td>-0.484612</td>
      <td>-0.717522</td>
      <td>-0.687850</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>0.355054</td>
      <td>0.300695</td>
      <td>-0.926397</td>
      <td>1.703721</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.759857</td>
      <td>0.366894</td>
      <td>-1.023559</td>
      <td>0.070350</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>-1.370062</td>
      <td>1.064458</td>
      <td>0.188206</td>
      <td>-0.977349</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.922617</td>
      <td>2.047103</td>
      <td>-2.533124</td>
      <td>0.690853</td>
    </tr>
  </tbody>
</table>
</div>



## Seleksi
Lihat dokumentasi pengindeksan [Indexing dan Memilih Data](http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing) dan [MultiIndex/Advanced Indexing](http://pandas.pydata.org/pandas-docs/stable/advanced.html#advanced).


```python
df['A']
df[0:3]
df['20130102':'20130104']
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <th>2013-01-02</th>
      <td>-0.257250</td>
      <td>-0.765153</td>
      <td>1.093545</td>
      <td>0.420117</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.922617</td>
      <td>2.047103</td>
      <td>-2.533124</td>
      <td>0.690853</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>0.355054</td>
      <td>0.300695</td>
      <td>-0.926397</td>
      <td>1.703721</td>
    </tr>
  </tbody>
</table>
</div>



## Seleksi Berdasarkan Label
Untuk mendapatkan penampang menggunakan label:


```python
df.loc[dates[0]]
```




    A    0.755035
    B   -0.484612
    C   -0.717522
    D   -0.687850
    Name: 2013-01-01 00:00:00, dtype: float64



Selecting on a multi-axis by label:


```python
df.loc[:,['A','B']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <th>2013-01-01</th>
      <td>0.755035</td>
      <td>-0.484612</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.257250</td>
      <td>-0.765153</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.922617</td>
      <td>2.047103</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>0.355054</td>
      <td>0.300695</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.759857</td>
      <td>0.366894</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>-1.370062</td>
      <td>1.064458</td>
    </tr>
  </tbody>
</table>
</div>



Menampilkan slicing label, kedua titik akhir disertakan:


```python
df.loc['20130102':'20130104',['A','B']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <th>2013-01-02</th>
      <td>-0.257250</td>
      <td>-0.765153</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.922617</td>
      <td>2.047103</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>0.355054</td>
      <td>0.300695</td>
    </tr>
  </tbody>
</table>
</div>



Pengurangan dimensi objek yang dikembalikan:


```python
df.loc['20130102',['A','B']]
```




    A   -0.257250
    B   -0.765153
    Name: 2013-01-02 00:00:00, dtype: float64



Untuk mendapatkan nilai skalar:


```python
df.loc[dates[0],'A']
```




    0.755034871161897



Untuk mendapatkan akses cepat ke skalar (setara dengan metode sebelumnya):


```python
df.at[dates[0],'A']
```




    0.755034871161897



## Selection by Position
Pilih melalui posisi bilangan bulat yang dilewati:


```python
df.iloc[3]
```




    A    0.355054
    B    0.300695
    C   -0.926397
    D    1.703721
    Name: 2013-01-04 00:00:00, dtype: float64



Dengan irisan integer, bertindak mirip dengan numpy / python:


```python
df.iloc[3:5,0:2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <th>2013-01-04</th>
      <td>0.355054</td>
      <td>0.300695</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.759857</td>
      <td>0.366894</td>
    </tr>
  </tbody>
</table>
</div>



Dengan daftar lokasi posisi bilangan bulat, mirip dengan gaya numpy / python:


```python
df.iloc[[1,2,4],[0,2]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-0.257250</td>
      <td>1.093545</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.922617</td>
      <td>-2.533124</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.759857</td>
      <td>-1.023559</td>
    </tr>
  </tbody>
</table>
</div>



For slicing rows explicitly:


```python
df.iloc[1:3,:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <th>2013-01-02</th>
      <td>-0.257250</td>
      <td>-0.765153</td>
      <td>1.093545</td>
      <td>0.420117</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.922617</td>
      <td>2.047103</td>
      <td>-2.533124</td>
      <td>0.690853</td>
    </tr>
  </tbody>
</table>
</div>



Untuk memotong kolom secara eksplisit:


```python
df.iloc[:,1:3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>-0.484612</td>
      <td>-0.717522</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.765153</td>
      <td>1.093545</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>2.047103</td>
      <td>-2.533124</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>0.300695</td>
      <td>-0.926397</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>0.366894</td>
      <td>-1.023559</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>1.064458</td>
      <td>0.188206</td>
    </tr>
  </tbody>
</table>
</div>



Untuk mendapatkan nilai secara eksplisit:


```python
df.iloc[1,1]
```




    -0.7651533932328203



Untuk mendapatkan akses cepat ke skalar (setara dengan metode sebelumnya):


```python
df.iat[1,1]
```




    -0.7651533932328203



## Boolean Indexing
Menggunakan nilai satu kolom untuk memilih data.


```python
df[df.A > 0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <th>2013-01-01</th>
      <td>0.755035</td>
      <td>-0.484612</td>
      <td>-0.717522</td>
      <td>-0.687850</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>0.355054</td>
      <td>0.300695</td>
      <td>-0.926397</td>
      <td>1.703721</td>
    </tr>
  </tbody>
</table>
</div>



Memilih nilai dari DataFrame di mana kondisi boolean terpenuhi.


```python
df[df > 0]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <th>2013-01-01</th>
      <td>0.755035</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.093545</td>
      <td>0.420117</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>NaN</td>
      <td>2.047103</td>
      <td>NaN</td>
      <td>0.690853</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>0.355054</td>
      <td>0.300695</td>
      <td>NaN</td>
      <td>1.703721</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>NaN</td>
      <td>0.366894</td>
      <td>NaN</td>
      <td>0.070350</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>NaN</td>
      <td>1.064458</td>
      <td>0.188206</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



Menggunakan metode `isin()` untuk memfilter:


```python
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2
df2[df2['E'].isin(['two','four'])]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-03</th>
      <td>-0.922617</td>
      <td>2.047103</td>
      <td>-2.533124</td>
      <td>0.690853</td>
      <td>two</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.759857</td>
      <td>0.366894</td>
      <td>-1.023559</td>
      <td>0.070350</td>
      <td>four</td>
    </tr>
  </tbody>
</table>
</div>



## Setting
Mengatur kolom baru secara otomatis menyelaraskan data dengan indeks.


```python
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
print(s1)
df['F'] = s1
```

    2013-01-02    1
    2013-01-03    2
    2013-01-04    3
    2013-01-05    4
    2013-01-06    5
    2013-01-07    6
    Freq: D, dtype: int64


Menetapkan nilai berdasarkan label:


```python
df.at[dates[0],'A'] = 0
```

Menetapkan nilai berdasarkan posisi:


```python
In [49]: df.iat[0,1] = 0
```

Pengaturan dengan menetapkan dengan array NumPy:


```python
In [50]: df.loc[:,'D'] = np.array([5] * len(df))
```

Hasil dari pengaturan operasi sebelumnya.


```python
df
df2 = df.copy()
df2[df2 > 0] = -df2
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.717522</td>
      <td>-5</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.257250</td>
      <td>-0.765153</td>
      <td>-1.093545</td>
      <td>-5</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.922617</td>
      <td>-2.047103</td>
      <td>-2.533124</td>
      <td>-5</td>
      <td>-2.0</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-0.355054</td>
      <td>-0.300695</td>
      <td>-0.926397</td>
      <td>-5</td>
      <td>-3.0</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-0.759857</td>
      <td>-0.366894</td>
      <td>-1.023559</td>
      <td>-5</td>
      <td>-4.0</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>-1.370062</td>
      <td>-1.064458</td>
      <td>-0.188206</td>
      <td>-5</td>
      <td>-5.0</td>
    </tr>
  </tbody>
</table>
</div>



## Missing Data
panda terutama menggunakan nilai np.nan untuk merepresentasikan data yang hilang. Secara default tidak termasuk dalam perhitungan.

Reindexing memungkinkan Anda mengubah / menambah / menghapus indeks pada sumbu tertentu. Ini mengembalikan salinan data.


```python
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.717522</td>
      <td>5</td>
      <td>NaN</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.257250</td>
      <td>-0.765153</td>
      <td>1.093545</td>
      <td>5</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.922617</td>
      <td>2.047103</td>
      <td>-2.533124</td>
      <td>5</td>
      <td>2.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>0.355054</td>
      <td>0.300695</td>
      <td>-0.926397</td>
      <td>5</td>
      <td>3.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



Untuk menjatuhkan setiap baris yang memiliki data yang hilang.


```python
df1.dropna(how='any')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-02</th>
      <td>-0.25725</td>
      <td>-0.765153</td>
      <td>1.093545</td>
      <td>5</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



Mengisi data yang hilang.


```python
df1.fillna(value=5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-0.717522</td>
      <td>5</td>
      <td>5.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>-0.257250</td>
      <td>-0.765153</td>
      <td>1.093545</td>
      <td>5</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-0.922617</td>
      <td>2.047103</td>
      <td>-2.533124</td>
      <td>5</td>
      <td>2.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>0.355054</td>
      <td>0.300695</td>
      <td>-0.926397</td>
      <td>5</td>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
  </tbody>
</table>
</div>



Untuk mendapatkan topeng boolean di mana nilai-nilai NaN.


```python
pd.isna(df1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
      <th>E</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## Operations
### Stats
Operasi secara umum mengecualikan data yang hilang. Melakukan statistik deskriptif:


```python
df.mean()
```




    A   -0.492455
    B    0.502333
    C   -0.653142
    D    5.000000
    F    3.000000
    dtype: float64



Operasi yang sama pada sumbu lainnya:


```python
df.mean(1)
```




    2013-01-01    1.070619
    2013-01-02    1.214228
    2013-01-03    1.118272
    2013-01-04    1.545870
    2013-01-05    1.516696
    2013-01-06    1.976520
    Freq: D, dtype: float64



Beroperasi dengan objek yang memiliki dimensi berbeda dan membutuhkan penyelarasan. Selain itu, panda secara otomatis disiarkan di sepanjang dimensi yang ditentukan.


```python
s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
s
df.sub(s, axis='index')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
      <th>F</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013-01-01</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-02</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2013-01-03</th>
      <td>-1.922617</td>
      <td>1.047103</td>
      <td>-3.533124</td>
      <td>4.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2013-01-04</th>
      <td>-2.644946</td>
      <td>-2.699305</td>
      <td>-3.926397</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2013-01-05</th>
      <td>-5.759857</td>
      <td>-4.633106</td>
      <td>-6.023559</td>
      <td>0.0</td>
      <td>-1.0</td>
    </tr>
    <tr>
      <th>2013-01-06</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Apply
Applying functions to the data:


```python
df.apply(np.cumsum)
df.apply(lambda x: x.max() - x.min())
```




    A    1.725117
    B    2.812256
    C    3.626668
    D    0.000000
    F    4.000000
    dtype: float64



### Histogramming
Lihat lebih lanjut di [Histogramming dan Discretization](http://pandas.pydata.org/pandas-docs/stable/basics.html#basics-discretization).


```python
s = pd.Series(np.random.randint(0, 7, size=10))
s
s.value_counts()
```




    1    3
    6    2
    5    1
    4    1
    3    1
    2    1
    0    1
    dtype: int64



### String Methods
Seri ini dilengkapi dengan satu set metode pemrosesan string di atribut str yang membuatnya mudah untuk beroperasi pada setiap elemen dari array, seperti pada potongan kode di bawah ini.

Perhatikan bahwa pencocokan pola dalam str umumnya menggunakan [regular expression](https://docs.python.org/3/library/re.html) secara default (dan dalam beberapa kasus selalu menggunakannya). Lihat lebih lanjut di [Vectorized String Methods](http://pandas.pydata.org/pandas-docs/stable/text.html#text-string-methods)


```python
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()
```




    0       a
    1       b
    2       c
    3    aaba
    4    baca
    5     NaN
    6    caba
    7     dog
    8     cat
    dtype: object




## Merge
### Concat
Pandas menyediakan berbagai fasilitas untuk dengan mudah menggabungkan bersama-sama Seri, DataFrame, dan objek Panel dengan berbagai jenis logika yang ditetapkan untuk indeks dan fungsionalitas aljabar relasional dalam kasus operasi gabungan / penggabungan.

Menggabungkan objek panda bersama dengan `concat()`:


```python
df = pd.DataFrame(np.random.randn(10, 4))
df
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.118427</td>
      <td>0.190108</td>
      <td>-0.453150</td>
      <td>-1.093824</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.015795</td>
      <td>-0.801392</td>
      <td>-0.558359</td>
      <td>-0.288907</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.258384</td>
      <td>1.954766</td>
      <td>1.324889</td>
      <td>2.252112</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.107187</td>
      <td>0.043142</td>
      <td>-2.979815</td>
      <td>0.572610</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.064760</td>
      <td>-1.481823</td>
      <td>0.427584</td>
      <td>0.612114</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1.882999</td>
      <td>0.217800</td>
      <td>-1.588313</td>
      <td>-1.320067</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.651584</td>
      <td>0.314119</td>
      <td>-0.889263</td>
      <td>1.692006</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-0.224523</td>
      <td>-0.280542</td>
      <td>0.015149</td>
      <td>0.894384</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.671175</td>
      <td>-0.811100</td>
      <td>0.446504</td>
      <td>0.242372</td>
    </tr>
    <tr>
      <th>9</th>
      <td>-0.398880</td>
      <td>0.562806</td>
      <td>-1.127063</td>
      <td>0.476283</td>
    </tr>
  </tbody>
</table>
</div>



### Join
Gaya gabungan SQL, lihat lebih lanjut [Database style joining](http://pandas.pydata.org/pandas-docs/stable/merging.html#merging-join)


```python
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
left
right
pd.merge(left, right, on='key')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>lval</th>
      <th>rval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>foo</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>foo</td>
      <td>2</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



Contoh lain yang bisa diberikan adalah:


```python
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
left
right
pd.merge(left, right, on='key')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>key</th>
      <th>lval</th>
      <th>rval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>foo</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bar</td>
      <td>2</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>



### Append
Tambahkan baris ke dataframe. Lihat bagian [Appending](http://pandas.pydata.org/pandas-docs/stable/merging.html#merging-concatenation).


```python
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
df
s = df.iloc[3]
df.append(s, ignore_index=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <td>0.866441</td>
      <td>-0.468115</td>
      <td>-0.737924</td>
      <td>-0.715929</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.185219</td>
      <td>1.530892</td>
      <td>1.620639</td>
      <td>0.948174</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.388351</td>
      <td>0.246904</td>
      <td>-0.044574</td>
      <td>0.825825</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-1.561208</td>
      <td>-0.747205</td>
      <td>-0.410400</td>
      <td>-0.572818</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.265459</td>
      <td>0.857843</td>
      <td>-1.642613</td>
      <td>-0.547174</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.925984</td>
      <td>0.721344</td>
      <td>0.881657</td>
      <td>0.263759</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.005163</td>
      <td>-0.025071</td>
      <td>-0.926894</td>
      <td>1.185703</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.156680</td>
      <td>1.671611</td>
      <td>0.871033</td>
      <td>-0.014317</td>
    </tr>
    <tr>
      <th>8</th>
      <td>-1.561208</td>
      <td>-0.747205</td>
      <td>-0.410400</td>
      <td>-0.572818</td>
    </tr>
  </tbody>
</table>
</div>



## Grouping
Dengan "group by" kami mengacu pada proses yang melibatkan satu atau lebih dari langkah-langkah berikut:
- Splitting
- Applying
- Combining


```python
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                            'foo', 'bar', 'foo', 'foo'],
                    'B' : ['one', 'one', 'two', 'three',
                            'two', 'two', 'one', 'three'],
                    'C' : np.random.randn(8),
                    'D' : np.random.randn(8)})
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <td>foo</td>
      <td>one</td>
      <td>-1.046118</td>
      <td>0.054247</td>
    </tr>
    <tr>
      <th>1</th>
      <td>bar</td>
      <td>one</td>
      <td>-0.014827</td>
      <td>-0.397806</td>
    </tr>
    <tr>
      <th>2</th>
      <td>foo</td>
      <td>two</td>
      <td>-0.654255</td>
      <td>-0.614107</td>
    </tr>
    <tr>
      <th>3</th>
      <td>bar</td>
      <td>three</td>
      <td>-0.101134</td>
      <td>1.922848</td>
    </tr>
    <tr>
      <th>4</th>
      <td>foo</td>
      <td>two</td>
      <td>0.987511</td>
      <td>-0.856157</td>
    </tr>
    <tr>
      <th>5</th>
      <td>bar</td>
      <td>two</td>
      <td>-2.081752</td>
      <td>0.334808</td>
    </tr>
    <tr>
      <th>6</th>
      <td>foo</td>
      <td>one</td>
      <td>-1.077867</td>
      <td>-1.456799</td>
    </tr>
    <tr>
      <th>7</th>
      <td>foo</td>
      <td>three</td>
      <td>0.592706</td>
      <td>-1.632559</td>
    </tr>
  </tbody>
</table>
</div>



Pengelompokan dan kemudian menerapkan fungsi `sum()` ke grup yang dihasilkan.


```python
df.groupby('A').sum()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>bar</th>
      <td>-2.197714</td>
      <td>1.859850</td>
    </tr>
    <tr>
      <th>foo</th>
      <td>-1.198022</td>
      <td>-4.505375</td>
    </tr>
  </tbody>
</table>
</div>



Pengelompokan berdasarkan beberapa kolom membentuk indeks hierarkis, dan lagi kita dapat menerapkan fungsi `sum`.


```python
df.groupby(['A','B']).sum()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th>B</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">bar</th>
      <th>one</th>
      <td>-0.014827</td>
      <td>-0.397806</td>
    </tr>
    <tr>
      <th>three</th>
      <td>-0.101134</td>
      <td>1.922848</td>
    </tr>
    <tr>
      <th>two</th>
      <td>-2.081752</td>
      <td>0.334808</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">foo</th>
      <th>one</th>
      <td>-2.123985</td>
      <td>-1.402551</td>
    </tr>
    <tr>
      <th>three</th>
      <td>0.592706</td>
      <td>-1.632559</td>
    </tr>
    <tr>
      <th>two</th>
      <td>0.333256</td>
      <td>-1.470265</td>
    </tr>
  </tbody>
</table>
</div>
