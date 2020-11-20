n = int(input('Introduceti n: '))
m = int(input('Introduceti m, m<n: '))
while (n % m == 0):
    n = n // m
if (n == 1):
    print('Numarul introdus este o putere a lui ', m)
else:
    print('Numarul introdus nu este o putere a lui ', m)