import pandas as pd
import random

# Создаем исходный DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразуем столбец "whoAmI" в one-hot формат
one_hot_encoded = pd.get_dummies(data['whoAmI'], prefix='whoAmI')

# Объединяем one-hot столбцы с исходным DataFrame
data_encoded = pd.concat([data, one_hot_encoded], axis=1)

# Выводим первые строки полученного DataFrame
data_encoded.head()