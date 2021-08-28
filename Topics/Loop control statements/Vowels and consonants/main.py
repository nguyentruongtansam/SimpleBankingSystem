chars = str(input())
vowels = list('aeiou')
for char in chars:
    if char.isalpha():
        print('vowel' if char in vowels else 'consonant')
    else:
        break
