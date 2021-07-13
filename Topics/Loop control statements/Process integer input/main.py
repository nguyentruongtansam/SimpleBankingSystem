# put your python code here
num_list = []
while True:
    num = int(input())
    if num < 10:
        continue
    elif num > 100:
        break
    else:
        num_list.append(num)
for num in num_list:
    print(num)
