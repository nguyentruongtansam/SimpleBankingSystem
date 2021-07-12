x = float(input())
y = float(input())

if x == 0 and y == 0:
    print("It's the origin!")
elif x == 0 or y == 0:
    print("One of the coordinates is equal to zero!")
elif x > 0 and y > 0:
    print('I')
elif x < 0 < y:
    print('II')
elif y < 0:
    print('III' if x < 0 else 'IV')
else:
    pass
