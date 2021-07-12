money = int(input())

if money // 6769 != 0:
    print(str(money // 6769) + ' sheep')
elif money // 3848 > 1:
    print(str(money // 3848) + ' cows')
elif money // 3848 != 0:
    print(str(money // 3848) + ' cow')
elif money // 1296 > 1:
    print(str(money // 1296) + ' pigs')
elif money // 1296 != 0:
    print(str(money // 1296) + ' pig')
elif money // 678 > 1:
    print(str(money // 678) + ' goats')
elif money // 678 != 0:
    print(str(money // 678) + ' goat')
elif money // 23 > 1:
    print(str(money // 23) + ' chickens')
elif money // 23 != 0:
    print(str(money // 23) + ' chicken')
else:
    print('None')
