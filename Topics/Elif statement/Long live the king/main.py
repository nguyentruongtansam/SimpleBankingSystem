column = int(input())
row = int(input())
if (1 <= column <= 8) and (1 <= row <= 8):
    block = 0
    if column in (1, 8):
        if row in (1, 8):
            block += 5
        else:
            block += 3
    elif row in (1, 8):
        if column in (1, 8):
            block += 5
        else:
            block += 3
    print(8 - block)
else:
    pass
