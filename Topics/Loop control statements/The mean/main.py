nums = list()
while True:
    x = input()
    if str(x) == '.':
        break
    nums.append(float(x))
print(sum(nums) / len(nums))
