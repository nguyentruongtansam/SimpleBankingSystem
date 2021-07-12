# import re
#
# name = input()
# name = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
# print(name)

lowerCamelCase = str(input())
snake_case = lowerCamelCase[1:]
for char in snake_case:
    if char.isupper():
        snake_case = snake_case.replace(char, '_' + char.lower())
print(lowerCamelCase[0].lower() + snake_case)
