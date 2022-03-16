a = 8
b = 7
if a > b:
    print('Liczba %(zm1)d jest większa od liczby %(zm2)d'%{'zm1':a, 'zm2':b})
elif a < b:
    print('Liczba %(zm1)d jest mniejsza od liczby %(zm2)d' % {'zm1': a, 'zm2': b})
else:
    print('Liczby %(zm1)d i %(zm2)d są równe' % {'zm1': a, 'zm2': b})

if a == b:
    print('Liczby %(zm1)d i %(zm2)d są równe' % {'zm1': a, 'zm2': b})
else:
    print('Liczby %(zm1)d i %(zm2)d są różne' % {'zm1': a, 'zm2': b})

a = input('Podaj liczbę: ')
print(a)
print(type(a))
a = int (a) #rzutowanie
print(a)
print(type(a))
b = int(input ('Podaj liczbę: '))
print(b)
print(type(b))
#if (a > b) & (c > d):

a = input('Podaj 1. liczbę: ') #kopiowanie linijki w dół: ctrl+d
b = input('Podaj 2. liczbę: ')
c = input('Podaj 3. liczbę: ')
d = input('Podaj 4. liczbę: ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if (a > b) & (c > d):
    print ('%(zm1)d jest większe od %(zm2)d i %(zm3)d jest większe od %(zm4)d' %{'zm1':a, 'zm2':b, 'zm3':c, 'zm4':d})
else:
    print ('%(zm1)d jest mniejsze od %(zm2)d lub %(zm3)d jest mniejsze od %(zm4)d' % {'zm1': a, 'zm2': b, 'zm3': c, 'zm4': d})

for a in range(0, 7, 1):
    print (a)

lista = [] #deklaracja pustej listy
lista = ['cos', 3, 4, 3.14]
for a in lista:
    print (a)
else:
    print ("Wyświetlono wszystkie elementy listy")

licznik = 0
while licznik != 11:
    print (licznik)
    licznik += 1

lista = [4, 8, 5, 3, 2, 9 , 7]
licznik = 0
liczba = input('Wpisz liczbę całkowitą: ')
while liczba != len(lista): #funckja len zwraca liczbę elementów listy
    if int(liczba) - lista[licznik] == 0:
        print('Liczba ' + str(liczba) + ' - ' + str(lista[licznik]) + ' = 0')
        break
    else: licznik += 1
else:
    print('Żadna z wartości nie dała odpowiedniego wyniku') #jeżeli zadziałał break to ten else jest pomijany

lista1 = [4, 6, 8, 1, 6, 7, 2, 9]
lista2 = [4, 7, 3, 5]
suma = []
for a in lista1:
    for b in lista2:
        wynik = a+b
        suma.append(wynik) #funkcja append dodaje wynik na koniec listy
    print (suma)

a = input("Podaj 1. liczbę: ")
b = input("Podaj 2. liczbę: ")
try:
    a = int(a)
    b = int(b)
    wynik = a/b
    print (wynik)
except ZeroDivisionError:
    print('Nie można dzielić przez zero.')
except ValueError:
    print('Nie wczytano liczby całkowitej.')

lista = [4, 3.14, [1, 2, 3], 'a', 'nie', 2]
slownik = {1:'ble', 2:30, 3:1.5, 'a':'b'}

print(lista)
print(slownik)

lista.append(slownik['a'])
print(lista)
slownik[4]=10

print(slownik)

lista.insert(slownik[2], slownik[4])
print(lista)

lista.pop(0) #usuwa pozycje o danym numerze z listy
slownik.pop(1)
print(lista)
print(slownik)

lista.remove('a') #usuwa podaną rzecz z listy
print(lista)
