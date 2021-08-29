num_list = []
while True:
    num = str(input())
    if num == '.':
        break
    else:
        num_list.append(float(num))
print(min(num_list))
