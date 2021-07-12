# put your code here
x = int(input())
count = 0
total = 0
while x != 55:
    count += 1
    total += x
    x = int(input())
print(count)
print(total)
print(round(total / count))
