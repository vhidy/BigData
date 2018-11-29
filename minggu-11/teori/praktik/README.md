## Data Analysis di Pandas
Kode pada praktik in dapat langsung dilihat hasilnya melalui [Jupyter Notebook](./Chapter_03_Beginning_Data_Analysis.ipynb) 

Berikut ini adalah kode sumber yang diambil dari buku dan dijadikan kode sumber terpisah per sub judul :
1. [Data Analysis Routine](./data_analysis_routine.py)
2. [Reducing Memory by Changing Data Types](./reducing_memory_by_changing_data_types.py)
3. [Selecting The Smallest of The Largest](./selecting_the_smallest_of_the_largest.py)
4. [Selecting The Largest of Each Group by Sorting](./selecting_the_largest_of_each_group_by_sorting.py)
5. [Replicating nlargest With sort_values](./replicating_nlargest_with_sort_values.py)
6. [Calculating a Trailing Stop Order Price](./calculating_a_trailing_stop_order_price.py)


Sebelum menjalankan kode perlu di impor dulu pustaka yang dibutuhkan
```python
import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50
```

### Data Analysis Routine
Di sub bab ini akan menggunakan dataset `college.csv` yang terdapat di direktori data untuk kebutuhan analisis sederhana
```python
college = pd.read_csv('data/college.csv')
print(college.head())
print(college.shape)

with pd.option_context('display.max_rows', 8):
    display(college.describe(include=[np.number]).T)

college.describe(include=[np.object, pd.Categorical]).T
print(college.info())

college.describe(include=[np.number]).T
college.describe(include=[np.object, pd.Categorical]).T

with pd.option_context('display.max_rows', 5):
    display(college.describe(include=[np.number], 
                 percentiles=[.01, .05, .10, .25, .5, .75, .9, .95, .99]).T)

college_dd = pd.read_csv('data/college_data_dictionary.csv')

with pd.option_context('display.max_rows', 8):
    display(college_dd)
```

#### Output
Berikut ini adalah keluaran dari kode diatas jika dijalankan
```
                                INSTNM        CITY STABBR  HBCU  MENONLY  \
0             Alabama A & M University      Normal     AL   1.0      0.0
1  University of Alabama at Birmingham  Birmingham     AL   0.0      0.0
2                   Amridge University  Montgomery     AL   0.0      0.0
3  University of Alabama in Huntsville  Huntsville     AL   0.0      0.0
4             Alabama State University  Montgomery     AL   1.0      0.0

   WOMENONLY  RELAFFIL  SATVRMID  SATMTMID  DISTANCEONLY     UGDS  UGDS_WHITE  \
0        0.0         0     424.0     420.0           0.0   4206.0      0.0333
1        0.0         0     570.0     565.0           0.0  11383.0      0.5922
2        0.0         1       NaN       NaN           1.0    291.0      0.2990
3        0.0         0     595.0     590.0           0.0   5451.0      0.6988
4        0.0         0     425.0     430.0           0.0   4811.0      0.0158

   UGDS_BLACK  UGDS_HISP  UGDS_ASIAN  UGDS_AIAN  UGDS_NHPI  UGDS_2MOR  \
0      0.9353     0.0055      0.0019     0.0024     0.0019     0.0000
1      0.2600     0.0283      0.0518     0.0022     0.0007     0.0368
2      0.4192     0.0069      0.0034     0.0000     0.0000     0.0000
3      0.1255     0.0382      0.0376     0.0143     0.0002     0.0172
4      0.9208     0.0121      0.0019     0.0010     0.0006     0.0098

   UGDS_NRA  UGDS_UNKN  PPTUG_EF  CURROPER  PCTPELL  PCTFLOAN  UG25ABV  \
0    0.0059     0.0138    0.0656         1   0.7356    0.8284   0.1049
1    0.0179     0.0100    0.2607         1   0.3460    0.5214   0.2422
2    0.0000     0.2715    0.4536         1   0.6801    0.7795   0.8540
3    0.0332     0.0350    0.2146         1   0.3072    0.4596   0.2640
4    0.0243     0.0137    0.0892         1   0.7347    0.7554   0.1270

  MD_EARN_WNE_P10 GRAD_DEBT_MDN_SUPP
0           30300              33888
1           39700            21941.5
2           40100              23370
3           45500              24097
4           26600            33118.5
(7535, 27)
            count      mean       std  min     25%      50%       75%  max
HBCU       7164.0  0.014238  0.118478  0.0  0.0000  0.00000  0.000000  1.0
MENONLY    7164.0  0.009213  0.095546  0.0  0.0000  0.00000  0.000000  1.0
WOMENONLY  7164.0  0.005304  0.072642  0.0  0.0000  0.00000  0.000000  1.0
RELAFFIL   7535.0  0.190975  0.393096  0.0  0.0000  0.00000  0.000000  1.0
...           ...       ...       ...  ...     ...      ...       ...  ...
CURROPER   7535.0  0.923291  0.266146  0.0  1.0000  1.00000  1.000000  1.0
PCTPELL    6849.0  0.530643  0.225544  0.0  0.3578  0.52150  0.712900  1.0
PCTFLOAN   6849.0  0.522211  0.283616  0.0  0.3329  0.58330  0.745000  1.0
UG25ABV    6718.0  0.410021  0.228939  0.0  0.2415  0.40075  0.572275  1.0

[22 rows x 8 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7535 entries, 0 to 7534
Data columns (total 27 columns):
INSTNM                7535 non-null object
CITY                  7535 non-null object
STABBR                7535 non-null object
HBCU                  7164 non-null float64
MENONLY               7164 non-null float64
WOMENONLY             7164 non-null float64
RELAFFIL              7535 non-null int64
SATVRMID              1185 non-null float64
SATMTMID              1196 non-null float64
DISTANCEONLY          7164 non-null float64
UGDS                  6874 non-null float64
UGDS_WHITE            6874 non-null float64
UGDS_BLACK            6874 non-null float64
UGDS_HISP             6874 non-null float64
UGDS_ASIAN            6874 non-null float64
UGDS_AIAN             6874 non-null float64
UGDS_NHPI             6874 non-null float64
UGDS_2MOR             6874 non-null float64
UGDS_NRA              6874 non-null float64
UGDS_UNKN             6874 non-null float64
PPTUG_EF              6853 non-null float64
CURROPER              7535 non-null int64
PCTPELL               6849 non-null float64
PCTFLOAN              6849 non-null float64
UG25ABV               6718 non-null float64
MD_EARN_WNE_P10       6413 non-null object
GRAD_DEBT_MDN_SUPP    7503 non-null object
dtypes: float64(20), int64(2), object(5)
memory usage: 1.6+ MB
None
           count      mean       std  min      1%      5%     10%     25%  \
HBCU      7164.0  0.014238  0.118478  0.0  0.0000  0.0000  0.0000  0.0000
MENONLY   7164.0  0.009213  0.095546  0.0  0.0000  0.0000  0.0000  0.0000
...          ...       ...       ...  ...     ...     ...     ...     ...
PCTFLOAN  6849.0  0.522211  0.283616  0.0  0.0000  0.0000  0.0000  0.3329
UG25ABV   6718.0  0.410021  0.228939  0.0  0.0025  0.0374  0.0899  0.2415

              50%       75%      90%      95%       99%  max
HBCU      0.00000  0.000000  0.00000  0.00000  1.000000  1.0
MENONLY   0.00000  0.000000  0.00000  0.00000  0.000000  1.0
...           ...       ...      ...      ...       ...  ...
PCTFLOAN  0.58330  0.745000  0.84752  0.89792  0.986368  1.0
UG25ABV   0.40075  0.572275  0.72666  0.80000  0.917383  1.0

[22 rows x 14 columns]
           column_name                                description
0               INSTNM                           Institution Name
1                 CITY                              City Location
2               STABBR                         State Abbreviation
3                 HBCU   Historically Black College or University
..                 ...                                        ...
23            PCTFLOAN         Percent Students with federal loan
24             UG25ABV             Percent Students Older than 25
25     MD_EARN_WNE_P10  Median Earnings 10 years after enrollment
26  GRAD_DEBT_MDN_SUPP                  Median debt of completers

[27 rows x 2 columns]
```


### Reducing Memory by Changing Data Types
Di sub bab ini akan mencoba mengurangi beban memori dengan cara mengubah tipe data pada struktur data DataFrame
```python
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
```

#### Output
Berikut ini adalah hasil keluaran jika kode diatas dijlankan
```
   RELAFFIL  SATMTMID  CURROPER                               INSTNM STABBR
0         0     420.0         1             Alabama A & M University     AL
1         0     565.0         1  University of Alabama at Birmingham     AL
2         1       NaN         1                   Amridge University     AL
3         0     590.0         1  University of Alabama in Huntsville     AL
4         0     430.0         1             Alabama State University     AL

RELAFFIL      int64
SATMTMID    float64
CURROPER      int64
INSTNM       object
STABBR       object
dtype: object

Index           80
RELAFFIL     60280
SATMTMID     60280
CURROPER     60280
INSTNM      660240
STABBR      444565
dtype: int64

RELAFFIL       int8
SATMTMID    float64
CURROPER      int64
INSTNM       object
STABBR       object
dtype: object

RELAFFIL        int8
SATMTMID     float64
CURROPER       int64
INSTNM        object
STABBR      category
dtype: object

Index           80
RELAFFIL      7535
SATMTMID     60280
CURROPER     60280
INSTNM      660699
STABBR       13576
dtype: int64

Index       1.000000
RELAFFIL    0.125000
SATMTMID    1.000000
CURROPER    1.000000
INSTNM      1.000695
STABBR      0.030538
dtype: float64

float64

Traceback (most recent call last):
  File "reducing_memory_by_changing_data_types.py", line 36, in <module>
    college['MENONLY'].astype('int8') # ValueError: Cannot convert non-finite values (NA or inf) to integer
  File "/home/idiot/.virtualenvs/bigdata/lib/python3.6/site-packages/pandas/util/_decorators.py", line 178, in wrapper
    return func(*args, **kwargs)
  File "/home/idiot/.virtualenvs/bigdata/lib/python3.6/site-packages/pandas/core/generic.py", line 5001, in astype
    **kwargs)
  File "/home/idiot/.virtualenvs/bigdata/lib/python3.6/site-packages/pandas/core/internals.py", line 3714, in astype
    return self.apply('astype', dtype=dtype, **kwargs)
  File "/home/idiot/.virtualenvs/bigdata/lib/python3.6/site-packages/pandas/core/internals.py", line 3581, in apply
    applied = getattr(b, f)(**kwargs)
  File "/home/idiot/.virtualenvs/bigdata/lib/python3.6/site-packages/pandas/core/internals.py", line 575, in astype
    **kwargs)
  File "/home/idiot/.virtualenvs/bigdata/lib/python3.6/site-packages/pandas/core/internals.py", line 664, in _astype
    values = astype_nansafe(values.ravel(), dtype, copy=True)
  File "/home/idiot/.virtualenvs/bigdata/lib/python3.6/site-packages/pandas/core/dtypes/cast.py", line 702, in astype_nansafe
    raise ValueError('Cannot convert non-finite values (NA or inf) to '
ValueError: Cannot convert non-finite values (NA or inf) to integer

               count         mean            std    min         25%  \
HBCU          7164.0     0.014238       0.118478    0.0    0.000000
MENONLY       7164.0     0.009213       0.095546    0.0    0.000000
WOMENONLY     7164.0     0.005304       0.072642    0.0    0.000000
RELAFFIL      7535.0     0.190975       0.393096    0.0    0.000000
SATVRMID      1185.0   522.819409      68.578862  290.0  475.000000
SATMTMID      1196.0   530.765050      73.469767  310.0  482.000000
DISTANCEONLY  7164.0     0.005583       0.074519    0.0    0.000000
UGDS          6874.0  2356.837940    5474.275871    0.0  117.000000
UGDS_WHITE    6874.0     0.510207       0.286958    0.0    0.267500
UGDS_BLACK    6874.0     0.189997       0.224587    0.0    0.036125
UGDS_HISP     6874.0     0.161635       0.221854    0.0    0.027600
UGDS_ASIAN    6874.0     0.033544       0.073777    0.0    0.002500
UGDS_AIAN     6874.0     0.013813       0.070196    0.0    0.000000
UGDS_NHPI     6874.0     0.004569       0.033125    0.0    0.000000
UGDS_2MOR     6874.0     0.023950       0.031288    0.0    0.000000
UGDS_NRA      6874.0     0.016086       0.050172    0.0    0.000000
UGDS_UNKN     6874.0     0.045181       0.093440    0.0    0.000000
PPTUG_EF      6853.0     0.226639       0.246470    0.0    0.000000
CURROPER      7535.0  1328.063172  115201.552429    0.0    1.000000
PCTPELL       6849.0     0.530643       0.225544    0.0    0.357800
PCTFLOAN      6849.0     0.522211       0.283616    0.0    0.332900
UG25ABV       6718.0     0.410021       0.228939    0.0    0.241500

                    50%          75%           max
HBCU            0.00000     0.000000  1.000000e+00
MENONLY         0.00000     0.000000  1.000000e+00
WOMENONLY       0.00000     0.000000  1.000000e+00
RELAFFIL        0.00000     0.000000  1.000000e+00
SATVRMID      510.00000   555.000000  7.650000e+02
SATMTMID      520.00000   565.000000  7.850000e+02
DISTANCEONLY    0.00000     0.000000  1.000000e+00
UGDS          412.50000  1929.500000  1.515580e+05
UGDS_WHITE      0.55570     0.747875  1.000000e+00
UGDS_BLACK      0.10005     0.257700  1.000000e+00
UGDS_HISP       0.07140     0.198875  1.000000e+00
UGDS_ASIAN      0.01290     0.032700  9.727000e-01
UGDS_AIAN       0.00260     0.007300  1.000000e+00
UGDS_NHPI       0.00000     0.002500  9.983000e-01
UGDS_2MOR       0.01750     0.033900  5.333000e-01
UGDS_NRA        0.00000     0.011700  9.286000e-01
UGDS_UNKN       0.01430     0.045400  9.027000e-01
PPTUG_EF        0.15040     0.376900  1.000000e+00
CURROPER        1.00000     1.000000  1.000000e+07
PCTPELL         0.52150     0.712900  1.000000e+00
PCTFLOAN        0.58330     0.745000  1.000000e+00
UG25ABV         0.40075     0.572275  1.000000e+00

               count         mean            std    min         25%  \
HBCU          7164.0     0.014238       0.118478    0.0    0.000000
MENONLY       7164.0     0.009213       0.095546    0.0    0.000000
WOMENONLY     7164.0     0.005304       0.072642    0.0    0.000000
RELAFFIL      7535.0     0.190975       0.393096    0.0    0.000000
SATVRMID      1185.0   522.819409      68.578862  290.0  475.000000
SATMTMID      1196.0   530.765050      73.469767  310.0  482.000000
DISTANCEONLY  7164.0     0.005583       0.074519    0.0    0.000000
UGDS          6874.0  2356.837940    5474.275871    0.0  117.000000
UGDS_WHITE    6874.0     0.510207       0.286958    0.0    0.267500
UGDS_BLACK    6874.0     0.189997       0.224587    0.0    0.036125
UGDS_HISP     6874.0     0.161635       0.221854    0.0    0.027600
UGDS_ASIAN    6874.0     0.033544       0.073777    0.0    0.002500
UGDS_AIAN     6874.0     0.013813       0.070196    0.0    0.000000
UGDS_NHPI     6874.0     0.004569       0.033125    0.0    0.000000
UGDS_2MOR     6874.0     0.023950       0.031288    0.0    0.000000
UGDS_NRA      6874.0     0.016086       0.050172    0.0    0.000000
UGDS_UNKN     6874.0     0.045181       0.093440    0.0    0.000000
PPTUG_EF      6853.0     0.226639       0.246470    0.0    0.000000
CURROPER      7535.0  1328.063172  115201.552429    0.0    1.000000
PCTPELL       6849.0     0.530643       0.225544    0.0    0.357800
PCTFLOAN      6849.0     0.522211       0.283616    0.0    0.332900
UG25ABV       6718.0     0.410021       0.228939    0.0    0.241500

                    50%          75%           max
HBCU            0.00000     0.000000  1.000000e+00
MENONLY         0.00000     0.000000  1.000000e+00
WOMENONLY       0.00000     0.000000  1.000000e+00
RELAFFIL        0.00000     0.000000  1.000000e+00
SATVRMID      510.00000   555.000000  7.650000e+02
SATMTMID      520.00000   565.000000  7.850000e+02
DISTANCEONLY    0.00000     0.000000  1.000000e+00
UGDS          412.50000  1929.500000  1.515580e+05
UGDS_WHITE      0.55570     0.747875  1.000000e+00
UGDS_BLACK      0.10005     0.257700  1.000000e+00
UGDS_HISP       0.07140     0.198875  1.000000e+00
UGDS_ASIAN      0.01290     0.032700  9.727000e-01
UGDS_AIAN       0.00260     0.007300  1.000000e+00
UGDS_NHPI       0.00000     0.002500  9.983000e-01
UGDS_2MOR       0.01750     0.033900  5.333000e-01
UGDS_NRA        0.00000     0.011700  9.286000e-01
UGDS_UNKN       0.01430     0.045400  9.027000e-01
PPTUG_EF        0.15040     0.376900  1.000000e+00
CURROPER        1.00000     1.000000  1.000000e+07
PCTPELL         0.52150     0.712900  1.000000e+00
PCTFLOAN        0.58330     0.745000  1.000000e+00
UG25ABV         0.40075     0.572275  1.000000e+00

               count         mean            std    min         25%  \
HBCU          7164.0     0.014238       0.118478    0.0    0.000000
MENONLY       7164.0     0.009213       0.095546    0.0    0.000000
WOMENONLY     7164.0     0.005304       0.072642    0.0    0.000000
SATVRMID      1185.0   522.819409      68.578862  290.0  475.000000
SATMTMID      1196.0   530.765050      73.469767  310.0  482.000000
DISTANCEONLY  7164.0     0.005583       0.074519    0.0    0.000000
UGDS          6874.0  2356.837940    5474.275871    0.0  117.000000
UGDS_WHITE    6874.0     0.510207       0.286958    0.0    0.267500
UGDS_BLACK    6874.0     0.189997       0.224587    0.0    0.036125
UGDS_HISP     6874.0     0.161635       0.221854    0.0    0.027600
UGDS_ASIAN    6874.0     0.033544       0.073777    0.0    0.002500
UGDS_AIAN     6874.0     0.013813       0.070196    0.0    0.000000
UGDS_NHPI     6874.0     0.004569       0.033125    0.0    0.000000
UGDS_2MOR     6874.0     0.023950       0.031288    0.0    0.000000
UGDS_NRA      6874.0     0.016086       0.050172    0.0    0.000000
UGDS_UNKN     6874.0     0.045181       0.093440    0.0    0.000000
PPTUG_EF      6853.0     0.226639       0.246470    0.0    0.000000
CURROPER      7535.0  1328.063172  115201.552429    0.0    1.000000
PCTPELL       6849.0     0.530643       0.225544    0.0    0.357800
PCTFLOAN      6849.0     0.522211       0.283616    0.0    0.332900
UG25ABV       6718.0     0.410021       0.228939    0.0    0.241500

                    50%          75%           max
HBCU            0.00000     0.000000  1.000000e+00
MENONLY         0.00000     0.000000  1.000000e+00
WOMENONLY       0.00000     0.000000  1.000000e+00
SATVRMID      510.00000   555.000000  7.650000e+02
SATMTMID      520.00000   565.000000  7.850000e+02
DISTANCEONLY    0.00000     0.000000  1.000000e+00
UGDS          412.50000  1929.500000  1.515580e+05
UGDS_WHITE      0.55570     0.747875  1.000000e+00
UGDS_BLACK      0.10005     0.257700  1.000000e+00
UGDS_HISP       0.07140     0.198875  1.000000e+00
UGDS_ASIAN      0.01290     0.032700  9.727000e-01
UGDS_AIAN       0.00260     0.007300  1.000000e+00
UGDS_NHPI       0.00000     0.002500  9.983000e-01
UGDS_2MOR       0.01750     0.033900  5.333000e-01
UGDS_NRA        0.00000     0.011700  9.286000e-01
UGDS_UNKN       0.01430     0.045400  9.027000e-01
PPTUG_EF        0.15040     0.376900  1.000000e+00
CURROPER        1.00000     1.000000  1.000000e+07
PCTPELL         0.52150     0.712900  1.000000e+00
PCTFLOAN        0.58330     0.745000  1.000000e+00
UG25ABV         0.40075     0.572275  1.000000e+00

               count         mean            std    min         25%  \
HBCU          7164.0     0.014238       0.118478    0.0    0.000000
MENONLY       7164.0     0.009213       0.095546    0.0    0.000000
WOMENONLY     7164.0     0.005304       0.072642    0.0    0.000000
RELAFFIL      7535.0     0.190975       0.393096    0.0    0.000000
SATVRMID      1185.0   522.819409      68.578862  290.0  475.000000
SATMTMID      1196.0   530.765050      73.469767  310.0  482.000000
DISTANCEONLY  7164.0     0.005583       0.074519    0.0    0.000000
UGDS          6874.0  2356.837940    5474.275871    0.0  117.000000
UGDS_WHITE    6874.0     0.510207       0.286958    0.0    0.267500
UGDS_BLACK    6874.0     0.189997       0.224587    0.0    0.036125
UGDS_HISP     6874.0     0.161635       0.221854    0.0    0.027600
UGDS_ASIAN    6874.0     0.033544       0.073777    0.0    0.002500
UGDS_AIAN     6874.0     0.013813       0.070196    0.0    0.000000
UGDS_NHPI     6874.0     0.004569       0.033125    0.0    0.000000
UGDS_2MOR     6874.0     0.023950       0.031288    0.0    0.000000
UGDS_NRA      6874.0     0.016086       0.050172    0.0    0.000000
UGDS_UNKN     6874.0     0.045181       0.093440    0.0    0.000000
PPTUG_EF      6853.0     0.226639       0.246470    0.0    0.000000
CURROPER      7535.0  1328.063172  115201.552429    0.0    1.000000
PCTPELL       6849.0     0.530643       0.225544    0.0    0.357800
PCTFLOAN      6849.0     0.522211       0.283616    0.0    0.332900
UG25ABV       6718.0     0.410021       0.228939    0.0    0.241500

                    50%          75%           max
HBCU            0.00000     0.000000  1.000000e+00
MENONLY         0.00000     0.000000  1.000000e+00
WOMENONLY       0.00000     0.000000  1.000000e+00
RELAFFIL        0.00000     0.000000  1.000000e+00
SATVRMID      510.00000   555.000000  7.650000e+02
SATMTMID      520.00000   565.000000  7.850000e+02
DISTANCEONLY    0.00000     0.000000  1.000000e+00
UGDS          412.50000  1929.500000  1.515580e+05
UGDS_WHITE      0.55570     0.747875  1.000000e+00
UGDS_BLACK      0.10005     0.257700  1.000000e+00
UGDS_HISP       0.07140     0.198875  1.000000e+00
UGDS_ASIAN      0.01290     0.032700  9.727000e-01
UGDS_AIAN       0.00260     0.007300  1.000000e+00
UGDS_NHPI       0.00000     0.002500  9.983000e-01
UGDS_2MOR       0.01750     0.033900  5.333000e-01
UGDS_NRA        0.00000     0.011700  9.286000e-01
UGDS_UNKN       0.01430     0.045400  9.027000e-01
PPTUG_EF        0.15040     0.376900  1.000000e+00
CURROPER        1.00000     1.000000  1.000000e+07
PCTPELL         0.52150     0.712900  1.000000e+00
PCTFLOAN        0.58330     0.745000  1.000000e+00
UG25ABV         0.40075     0.572275  1.000000e+00
60280
                                  movie_title  imdb_score       budget
0                                      Avatar         7.9  237000000.0
1    Pirates of the Caribbean: At World's End         7.1  300000000.0
2                                     Spectre         6.8  245000000.0
3                       The Dark Knight Rises         8.5  250000000.0
4  Star Wars: Episode VII - The Force Awakens         7.1          NaN

                   movie_title  imdb_score      budget
2725          Towering Inferno         9.5         NaN
1920  The Shawshank Redemption         9.3  25000000.0
3402             The Godfather         9.2   6000000.0
2779                   Dekalog         9.1         NaN
4312      Kickboxer: Vengeance         9.1  17000000.0

               movie_title  imdb_score    budget
4804        Butterfly Girl         8.7  180000.0
4801    Children of Heaven         8.5  180000.0
4706          12 Angry Men         8.9  350000.0
4550          A Separation         8.4  500000.0
4636  The Other Dream Team         8.4  500000.0
```


### Selecting The Smallest of The Largest
Di sub bab ini akan menggunakan dataset `movie.csv` yang dapat ditemukan di direktori data, untuk kebutuhan menampilkan pengurutan data
```python
movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
print(movie2.head())
print(movie2.nlargest(100, 'imdb_score').head())
print(movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget'))
```

#### Output
Berikut ini adalah hasil keluaran dari kode diatas jika dijalankan
```
                                  movie_title  imdb_score       budget
0                                      Avatar         7.9  237000000.0
1    Pirates of the Caribbean: At World's End         7.1  300000000.0
2                                     Spectre         6.8  245000000.0
3                       The Dark Knight Rises         8.5  250000000.0
4  Star Wars: Episode VII - The Force Awakens         7.1          NaN

                   movie_title  imdb_score      budget
2725          Towering Inferno         9.5         NaN
1920  The Shawshank Redemption         9.3  25000000.0
3402             The Godfather         9.2   6000000.0
2779                   Dekalog         9.1         NaN
4312      Kickboxer: Vengeance         9.1  17000000.0

               movie_title  imdb_score    budget
4804        Butterfly Girl         8.7  180000.0
4801    Children of Heaven         8.5  180000.0
4706          12 Angry Men         8.9  350000.0
4550          A Separation         8.4  500000.0
4636  The Other Dream Team         8.4  500000.0
```


### Selecting The Largest of Each Group by Sorting
Di sub bab ini masih menggunakan dataset `movie.csv` untuk keperluan pengurutan data dari besar ke kecil dengan pengelompokan data group by
```python
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
```

#### Output
Berikut ini adalah hasil keluaran dari program diatas
```
                                  movie_title  imdb_score       budget
0                                      Avatar         7.9  237000000.0
1    Pirates of the Caribbean: At World's End         7.1  300000000.0
2                                     Spectre         6.8  245000000.0
3                       The Dark Knight Rises         8.5  250000000.0
4  Star Wars: Episode VII - The Force Awakens         7.1          NaN

                   movie_title  imdb_score      budget
2725          Towering Inferno         9.5         NaN
1920  The Shawshank Redemption         9.3  25000000.0
3402             The Godfather         9.2   6000000.0
2779                   Dekalog         9.1         NaN
4312      Kickboxer: Vengeance         9.1  17000000.0

               movie_title  imdb_score    budget
4804        Butterfly Girl         8.7  180000.0
4801    Children of Heaven         8.5  180000.0
4706          12 Angry Men         8.9  350000.0
4550          A Separation         8.4  500000.0
4636  The Other Dream Team         8.4  500000.0

                       movie_title  title_year  imdb_score
3884                      The Veil      2016.0         4.7
2375    My Big Fat Greek Wedding 2      2016.0         6.1
2794          Miracles from Heaven      2016.0         6.8
92    Independence Day: Resurgence      2016.0         5.5
153                Kung Fu Panda 3      2016.0         7.2
                      movie_title  title_year  imdb_score
4312         Kickboxer: Vengeance      2016.0         9.1
4277  A Beginner's Guide to Snuff      2016.0         8.7
3798                      Airlift      2016.0         8.5
27     Captain America: Civil War      2016.0         8.2
98            Godzilla Resurgence      2016.0         8.2

                                  movie_title  title_year  imdb_score
4312                     Kickboxer: Vengeance      2016.0         9.1
3745                          Running Forever      2015.0         8.6
4369                   Queen of the Mountains      2014.0         8.7
3935  Batman: The Dark Knight Returns, Part 2      2013.0         8.4
3                       The Dark Knight Rises      2012.0         8.5
```


### Replicating nlargest with sort_values
Di sub bab ini akan menggunakan dataset yang sama seperti program di sub bab sebelumnya untuk menggandakan nilai terbesar menggunakan method `sort_values`
```python
movie = pd.read_csv('data/movie.csv')
movie2 = movie[['movie_title', 'imdb_score', 'budget']]
movie_smallest_largest = movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget')
print(movie_smallest_largest)
print(movie2.sort_values('imdb_score', ascending=False).head(100).head())
print(movie2.sort_values('imdb_score', ascending=False).head(100).sort_values('budget').head())
print(movie2.nlargest(100, 'imdb_score').tail())
print(movie2.sort_values('imdb_score', ascending=False).head(100).tail())
```

#### Output
Berikut ini adalah hasil keluaran dari program diatas
```
               movie_title  imdb_score    budget
4804        Butterfly Girl         8.7  180000.0
4801    Children of Heaven         8.5  180000.0
4706          12 Angry Men         8.9  350000.0
4550          A Separation         8.4  500000.0
4636  The Other Dream Team         8.4  500000.0
                   movie_title  imdb_score      budget
2725          Towering Inferno         9.5         NaN
1920  The Shawshank Redemption         9.3  25000000.0
3402             The Godfather         9.2   6000000.0
2779                   Dekalog         9.1         NaN
4312      Kickboxer: Vengeance         9.1  17000000.0
                    movie_title  imdb_score    budget
4815  A Charlie Brown Christmas         8.4  150000.0
4801         Children of Heaven         8.5  180000.0
4804             Butterfly Girl         8.7  180000.0
4706               12 Angry Men         8.9  350000.0
4636       The Other Dream Team         8.4  500000.0
                movie_title  imdb_score     budget
4023                 Oldboy         8.4  3000000.0
4163  To Kill a Mockingbird         8.4  2000000.0
4395         Reservoir Dogs         8.4  1200000.0
4550           A Separation         8.4   500000.0
4636   The Other Dream Team         8.4   500000.0
                                  movie_title  imdb_score      budget
3799                     Anne of Green Gables         8.4         NaN
3777                      Requiem for a Dream         8.4   4500000.0
3935  Batman: The Dark Knight Returns, Part 2         8.4   3500000.0
4636                     The Other Dream Team         8.4    500000.0
2455                                   Aliens         8.4  18500000.0
```


### Calculating a Trailing Stop Order Price
Di sub bab ini akan menggunakan pustaka tambahan yaitu `pandas_datareader` untuk men-_trail_ data
```python
import pandas_datareader as pdr

tsla = pdr.DataReader('tsla', data_source='yahoo',start='2017-1-1')
print(tsla.head(8))

tsla_close = tsla['Close']
tsla_cummax = tsla_close.cummax()
print(tsla_cummax.head(8))

tsla_trailing_stop = tsla_cummax * .9
print(tsla_trailing_stop.head(8))

def set_trailing_loss(symbol, purchase_date, perc):
    close = pdr.DataReader(symbol, 'yahoo', start=purchase_date)['Close']
    return close.cummax() * perc

msft_trailing_stop = set_trailing_loss('msft', '2017-6-1', .85)
print(msft_trailing_stop.head())
```

#### Output
Berikut ini adalah hasil keluaran dari program diatas
```
                  High         Low        Open       Close    Volume  \
Date
2017-01-03  220.330002  210.960007  214.860001  216.990005   5923300
2017-01-04  228.000000  214.309998  214.750000  226.990005  11213500
2017-01-05  227.479996  221.949997  226.419998  226.750000   5911700
2017-01-06  230.309998  225.449997  226.929993  229.009995   5527900
2017-01-09  231.919998  228.000000  228.970001  231.279999   3957000
2017-01-10  232.000000  226.889999  232.000000  229.869995   3660000
2017-01-11  229.979996  226.679993  229.070007  229.729996   3650800
2017-01-12  230.699997  225.580002  229.059998  229.589996   3790200

             Adj Close
Date
2017-01-03  216.990005
2017-01-04  226.990005
2017-01-05  226.750000
2017-01-06  229.009995
2017-01-09  231.279999
2017-01-10  229.869995
2017-01-11  229.729996
2017-01-12  229.589996

Date
2017-01-03    216.990005
2017-01-04    226.990005
2017-01-05    226.990005
2017-01-06    229.009995
2017-01-09    231.279999
2017-01-10    231.279999
2017-01-11    231.279999
2017-01-12    231.279999
Name: Close, dtype: float64

Date
2017-01-03    195.291005
2017-01-04    204.291005
2017-01-05    204.291005
2017-01-06    206.108995
2017-01-09    208.151999
2017-01-10    208.151999
2017-01-11    208.151999
2017-01-12    208.151999
Name: Close, dtype: float64

Date
2017-05-31    59.363997
2017-06-01    59.584999
2017-06-02    60.996002
2017-06-05    61.437999
2017-06-06    61.641997
Name: Close, dtype: float64
```
