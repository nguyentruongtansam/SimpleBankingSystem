num_list = []
while True:
    num = input()
    if str(num) == '.':
        break
    else:
        num_list.append(float(num))
print(min(num_list))
