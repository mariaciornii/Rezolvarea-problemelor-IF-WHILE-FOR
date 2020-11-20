an=int(input('Anul: '))
an -= 2000
if an % 12 == 0:
    print('Anul se numeste dragon')
elif an % 12 == 1:
    print('Anul se numeste sarpe')
elif an % 12 == 2:
    print('Anul se numeste cal')
elif an % 12 == 3:
    print('Anul se numeste oaie')
elif an % 12 == 4:
    print('Anul se numeste maimuta')
elif an % 12 == 5:
    print('Anul se numeste cocos')
elif an % 12 == 6:
    print('Anul se numeste caine')
elif an % 12 == 7:
    print('Anul se numeste porc')
elif an % 12 == 8:
    print('Anul se numeste sobolan')
elif an % 12 == 9:
    print('Anul se numeste bou')
elif an % 12 == 10:
    print('Anul se numeste tigru')
else:
    print('Anul se numeste iepure')