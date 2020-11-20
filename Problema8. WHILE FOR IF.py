a=int(input('a = '))
b=int(input('b = '))
c=int(input('c = '))
if (a<b+c) and (b<a+c) and (c<a+b):
    if (a==b) or (b==c) or (a==c):
        print('Exista asa triunghi si se numeste isoscel')
    elif a==b==c:
        print('Exista asa triunghi si se numeste echilateral')
    else:
        print('Exista asa triunghi si se numeste scalen')
else:
    print('Nu exista triunghi cu asa laturi')