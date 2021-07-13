word = str(input())
reverse = ''
# if len(word) % 2 == 0:
index = len(word)
while index > 0:
    reverse += word[index - 1]
    index -= 1
print('Palindrome' if word == reverse else 'Not palindrome')
# else:
#     pass
