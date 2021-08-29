cafes = []
while True:
    cafe = input()
    if cafe == 'MEOW':
        break
    cafes.append(cafe)

max_cafe_name = cafes[0].split(' ')[0]
max_cat_num = int(cafes[0].split(' ')[1])
for cafe in cafes:
    cafe_name = cafe.split(' ')[0]
    cat_num = int(cafe.split(' ')[1])
    if cat_num > max_cat_num:
        max_cat_num = cat_num
        max_cafe_name = cafe_name

print(max_cafe_name)
