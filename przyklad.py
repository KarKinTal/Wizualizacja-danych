import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Zadanie 1
dane1 = pd.Series([35, 47, 15, 41, 40], index=['A', 'B', 'C', 'D', 'E'])
dane2 = pd.Series([(-30), (-33), (-38), (-35), (-30)], index=['A', 'B', 'C', 'D', 'E'])
plt.subplot(1, 2, 1)
plt.barh(data=dane1, y=dane1.index, width=dane1.values,
         color=['lightblue', 'pink', 'orange', 'grey', 'purple'])
plt.title("Wykres lewy")
plt.subplot(1, 2, 2)
plt.barh(data=dane2, y=dane2.index, width=dane2.values,
         color=['magenta', 'aqua', 'cyan', 'brown', 'khaki'])
plt.title("Wykres prawy")
plt.savefig('zadanie1.png')
plt.show()

# Zadanie 2
ceny_xlsx = pd.ExcelFile('ceny2.xlsx')
ceny = pd.read_excel(ceny_xlsx, header=0)

print(ceny.groupby('Rodzaje towarów').agg({'Wartość':['mean']}))

ryz = ceny[ceny['Rodzaje towarów'] == 'ryż - za 1kg']
maka = ceny[ceny['Rodzaje towarów'] == 'mąka pszenna - za 1kg']
plt.plot(ryz['Rok'], ryz['Wartość'], label='Wartość ryżu')
plt.plot(maka['Rok'], maka['Wartość'], label='Wartość mąki')
plt.xlabel('Rok')
plt.ylabel('Wartość w zł za kg')
plt.title('Wartość w zł za kg mąki i ryżu w poszczególnych latach')
plt.xticks(ceny['Rok'])
plt.legend()

plt.text(2011, 2, '166334')

plt.savefig('zadanie2.jpg')
plt.show()

# # Zadanie 3
# nier = pd.read_csv('nieruchomosci2.csv', header=0, sep=';', decimal='.')
# print(nier)
# # nier = nier.transpose()
# print(nier.loc[0])
#


