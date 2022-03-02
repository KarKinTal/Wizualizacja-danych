#zadanie 1
zm_d1, zm_d2 = 2, 4
zm_f1, zm_f2 = 1.5, 0.125
zm_s1, zm_s2 = 'herbata', 'kawa'
zm_c1, zm_c2 = 2+1j, 3+2j
print('Intiger: %(z1)d, %(z2)d' %{'z1':zm_d1, 'z2':zm_d2})
print('Float: %(z1)f, %(z2)f' %{'z1':zm_f1, 'z2':zm_f2})
print('String: %(z1)s, %(z2)s' %{'z1':zm_s1, 'z2':zm_s2})
print('Complex: ')
print(zm_c1)
print(zm_c2)

#zadanie 2
zm1 = input ("Podaj 1. liczbę: ")
zm2 = input ("Podaj 2. liczbę: ")
print('''Możliwe operacje:
1 - dodawanie
2 - odejmowanie
3 - mnożenie
4 - dzielenie
5 - potęgowanie
6 - dzielenie całkowite
7 - reszta z dzielenia''')
op = input ("Wybierz operacje (1-7): ")

if op == '1':
    wynik = int(zm1) + int(zm2)
    print(wynik)
elif op == '2':
    wynik = int(zm1) - int(zm2)
    print(wynik)
elif op == '3':
    wynik = int(zm1) * int(zm2)
    print(wynik)
elif op == '4':
    wynik = int(zm1) / int(zm2)
    print(wynik)
elif op == '5':
    wynik = int(zm1) ** int(zm2)
    print(wynik)
elif op == '6':
    wynik = int(zm1) // int(zm2)
    print(wynik)
elif op == '7':
    wynik = int(zm1) % int(zm2)
    print(wynik)
else:
    print("Nieprawidlowy operator.")

#zadanie 3

#zadanie 4
import math
print(math.pow(math.log(5 + math.pow(math.sin(8), 2)), 1/6))

#zadanie 5
imie = "KAROLINA"
nazwisko = "TALAREK"
print (imie.capitalize() + " " + nazwisko.capitalize())

#zadanie 6
tekst = "la la la"
print (tekst.count("la"))

#zadanie 7
napis_dowolny = "Wieczko od słoika"
print(napis_dowolny)
print("Druga litera: " + napis_dowolny[1])
print("Ostatnia litera: " + napis_dowolny[-1:])

#zadanie 8
print(tekst.split())

#zadanie 9
zs = "pomidor"
zf = 3.14
z16 = hex(26)
print("%(zm1)s, %(zm2)f, %(zm3)s" %{"zm1":zs, "zm2":zf, "zm3":z16})

liczba_szesnastkowa = 0x1f
print('{0:x}'.format(liczba_szesnastkowa))
