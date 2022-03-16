import sys
import math

print (sys.version)
print ('cos')

a = 'informatyka ogólna grupa 4'
print (a)

b = 5
print (b)
print (type(b))

c = 5.4
print (c)

d = 3+2j
print (d)

nazwa_zmiennej = 'gites' #nazwy zlozone tworzymy za pomocą '_'

del a #usuwanie zmiennej

#del b #blok komentarzy to ctrl+slash
#print (b)

e,f = 3.14, 5
print (e+f)
g = 2
print (f // g)#dzielenie calkowite
print (f ** g)#potegowanie (wynik int)
print (math.pow(f,g))#potegowanie za pomoca funkcji z biblioteki math (wynik float)


a = 5
b = 3
c = 5-3
print ("wynik działania %(z1)d - %(z2)d = %(z3)d" % {'z1':a, 'z2':b, 'z3':c}) #sformatowany łańcuch)