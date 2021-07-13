# put your python code here
a = int(input())
b = int(input())
dividends = list()
for i in range (a, b + 1):
    if i % 3 == 0:
        dividends.append(i)
print(sum(dividends) / len(dividends))
