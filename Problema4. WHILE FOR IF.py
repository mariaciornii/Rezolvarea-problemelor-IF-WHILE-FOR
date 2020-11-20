from fractions import Fraction
a = int(input('Introduceti primul numarator: '))
b = int(input('Introduceti primul numitor: '))
c = int(input('Introduceti al doilea numarator: '))
d = int(input('Introduceti al doilea numitor: '))
s = Fraction(a,b) + Fraction(c,d)   
p = Fraction(a,b) * Fraction(c,d)   
print('a) suma este', s)   
print('b) produsul este', p)     