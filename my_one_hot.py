import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

hum = 'human'
rob = 'robot'
col = 'whoAmI'

data_one_hot = pd.DataFrame({}, columns=[hum, rob])
data_one_hot[hum] = data[(data[col]) != ''] == hum
data_one_hot[rob] = data[(data[col]) != ''] == rob
data_one_hot

