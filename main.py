import math

a = []
for x in range(0, 10):
    a.append(x**2)
print(a)
a2 = [x**2 for x in range(0, 10)]
print(a2)

b = []
for x in range(0, 6):
    b.append(3**x)
print(b)
b2 = [3**x for x in range(0, 6)]
print(b2)

c = []
for x in a:
    if x % 2 == 1:
        c.append(x)
print(c)
c2 = [x for x in a if x % 2 == 1]
print(c2)

# ZAGNIEŻDŻENIA

lista = []
for a in [1, 2, 3]:
    for b in [4, 5, 6]:
        lista.append((a, b))
print(lista)
lista2 = [(a, b) for a in [1, 2, 3] for b in [4, 5, 6]]
print(lista2)

slownik = {'PZU': 'Państwowy zaklad ubezpieczeń',
           'ZUS': 'Zakład ubezpieczeń społecznych',
           'PKO': 'Państwowa kasa oszczędności'}
slownik_odwrocony = {}
print(slownik)
for key, value in slownik.items():
    slownik_odwrocony[value] = key
print(slownik_odwrocony)
slownik2 = {value: key for key, value in slownik.items()}
print(slownik2)

# DEFINICJE FUNKCJI

def row_kwadratowe (a, b, c):
    delta = b**2 - 4 * a * c
    if delta < 0:
        print('Brak rozwiązań')
        return -1
    elif delta == 0:
        print('Jedno rozwiązanie:')
        x = (-b)/(2 * a)
        return x
    else:
        print('Dwa rozwiązania:')
        x1 = ((-b) - math.sqrt(delta))/(2 * a)
        x2 = ((-b) + math.sqrt(delta))/(2 * a)
        return x1, x2

print(row_kwadratowe(6, 1, 3))
print(row_kwadratowe(1, 2, 1))
print(row_kwadratowe(1, 4, 1))

def czy_parzysta (x):
    if x % 2 == 0:
        return 'Liczba jest parzysta'
    else:
        return 'Liczba jest nieparzysta'

print(czy_parzysta(7))
print(czy_parzysta(4))

def dl_odcinka(x1=1, y1=2, x2=3, y2=4):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
# argumenty domyślne
print(dl_odcinka())
# argumenty pozycyjne
print(dl_odcinka(4, 5, 6, 9))
# dwa argumenty pozycyjne, dwa określone
print(dl_odcinka(2, 2, y2=7, x2=5))
# argumenty po za kolejnością
print(dl_odcinka(x2=6, y2=4, x1=2, y1=3))
# dwa argumnety domyślne, dwa z nowa wartością
print(dl_odcinka(x2=4, y2=7))

def ciag(* liczby): # * - dowolna ilośc wartościowań
    if len(liczby) == 0:
        return 0
    else:
        suma = 0
        for i in liczby:
            suma += i
        return suma

print(ciag())
print(ciag(1, 2, 3, 4, 5, 6, 7, 8))

def co_lubie(** rzeczy): ## ** - dowolna ilośc argumentów z kluczem
    for cos in rzeczy:
        print('to jest')
        print(cos)
        print('co lubie')
        print(rzeczy[cos])
# cos - klucz, rzeczy[cos] - wartość na pozycji
co_lubie(gry=['planszowe', 'kąkuterowe'], slodycze='czekolada')

