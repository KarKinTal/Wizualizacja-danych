import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# # seaborn
# # wykres liniowy
# sns.set(rc={'figure.figsize': (8, 8)})
# sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16],
#              label='linia nr1', color='red',
#              marker='o', linestyle=':')
# sns.lineplot(x=[1, 2, 3, 4], y=[2, 5, 10, 17],
#              label='linia nr2', color='green',
#              marker='^', linestyle=':')
# plt.xlabel('oś x')
# plt.ylabel('oś y')
# plt.title('Wykres liniowy')
# plt.show()
#
# # wykres liniowy v2
# s = pd.Series(np.random.randn(1000))
# s = s.cumsum()
# sns.set()
# wykres = sns.relplot(kind='line', data=s, label='linia')
# wykres.fig.set_size_inches(8,6)
# wykres.fig.suptitle('Wykres liniowy losowych danych')
# wykres.set_xlabels('indeksy')
# wykres.set_ylabels('wartości')
# wykres.add_legend()
# wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)
# plt.show()
#
# # wykres liniowy v3
# sns.set()
# df = pd.read_csv('iris.csv', header=0, sep=',', decimal='.')
# print(df)
# wykres = sns.lineplot(data=df, x=df.index, y='sepal length', hue='class', palette=['pink', 'purple', 'magenta'])
# wykres.set_xlabel('indeksy')
# wykres.set_title('Wykres liniowy danych z Iris dataset')
# wykres.legend(title='Rodzaj kwiatu')
# plt.show()
#
# # wykres punktowy
# sns.set()
# data = {'a': np.arange(10),
#         'c': np.random.randint(0, 50, 10),
#         'd': np.random.randn(10)}
# data['b'] = data['a'] + 10 * np.random.randn(10)
# data['d'] = np.abs(data['d']) * 100
# print(data['c'])
# print(data['d'])
# df = pd.DataFrame(data)
# plot = sns.relplot(data=df, x="a", y="b",
#                    hue="c", palette='bright',
#                    size="d", legend=True)
# plot.fig.set_size_inches(6, 6)
# plot.set(xticks=data['a'])  # ustawienie jednostek na osi x
# plt.show()
#
# # wykres kolumnowy
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data)
# sns.set()
# plot = sns.barplot(data=df, x='Kontynent', y='Populacja',
#                    ci=None, hue='Kontynent', estimator=np.sum,
#                    dodge=False, palette=['blue', 'aquamarine', 'green'])  # estimator .sum - sumuje emelemnty w grupie
# plot.legend(title='Populacja na kontynentach')
# plot.set(title='Wykres słupkowy')
# plt.show()

# wykresy 3D
# # wykres liniowy
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# print(type(ax))
# t = np. linspace(0, 2 * np.pi, 100)
# z = t
# x = np.sin(t) * np.cos(t)
# y = np.tan(t)
# ax.plot(x, y, z, label='zadanie 1')
# ax.legend()
# plt.show()

# # wykres punktowy - nie skończony
# np.random.seed(19680801)
# def randrange(n, vmin, vmax):
#     """ Funkcja wspomagająca może tworzyć macierz losowych liczb"""
#     return (vmax - vmin) * np.random.rand(n) + vmin
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# n = 100
# # Dla każdego zbioru styli i zakresów wygeneruje n losowych punktów
# # zdefiniowane przez x z [23, 32], y z [0, 100], z z [zlow, zhigh].
# for c, m zlow, zhigh in [('r', 'o', -50)]
