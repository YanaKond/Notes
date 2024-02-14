import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

#pd.get_dummies(data['whoAmI'])

values = {'robot': 0, 'human': 1}
data['result'] = data['whoAmI'].map(values)

print(data.head())