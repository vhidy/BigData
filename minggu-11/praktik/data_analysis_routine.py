import pandas as pd
import numpy as np
from IPython.display import display
pd.options.display.max_columns = 50


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
