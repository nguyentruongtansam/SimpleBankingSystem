utc = int(input())
time = 10.5
if utc == 0:
    print('Tuesday')
else:
    if 1 <= utc <= 14:
        if time + utc >= 24:
            print('Wednesday')
        else:
            print('Tuesday')
    elif -12 <= utc <= -1:
        if time + utc < 0:
            print('Monday')
        else:
            print('Tuesday')
    else:
        pass
