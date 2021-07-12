string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
vowels_num = 0
for char in string:
    if char in list(vowels):
        vowels_num += 1
print(vowels_num)