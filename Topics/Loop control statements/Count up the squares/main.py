# put your python code here
add = 0
num_list = []
sum_square = 0
while True:
    num = int(input())
    num_list.append(num)
    if num_list[0] == 0:
        break
    else:
        add += num
        sum_square += num ** 2
    if add == 0:
        break
print(0 if num_list[0] == 0 else int(sum_square))
