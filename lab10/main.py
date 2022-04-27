import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# WYKRES LINIOWY
# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.savefig('wykres.png')
# plt.show()

# WYKRES KOLUMNOWY
# dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}
#
# df = pd.DataFrame(dane)
# grupa =  df.groupby('Kontynent').agg({'Populacja': ['sum']})
#
# grupa.plot(kind='bar', ylabel='Populacja', xlabel='Kontynet', rot=0, legend=True, title='Populacja dla kontynentów',
#            color='purple')  # plot z pandas
# plt.legend(loc='upper left')
# plt.grid()
# plt.show()

# WYKRES KOŁOWY
# df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
# print(df)
#
# grupa = df.groupby('Imię i nazwisko').agg({'Wartość zamówienia': ['sum']})
# print(grupa)
#
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
#     # zamiast subplot=True moze być np. y = 'Wartość zamówienia'
# plt.legend(loc='upper left')
# plt.show()

# WYKRES LINIOWY (inny)
ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()

df = pd.DataFrame(ts)
print(df)
df['Średnia krocząca'] = df.rolling(window=100).mean()
print(df)
df.plot()
plt.legend(['Wartości', 'Średnia krocząca'])
plt.show()