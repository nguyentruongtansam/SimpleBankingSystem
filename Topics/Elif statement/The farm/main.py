money = int(input())

animals = {'chicken': 23,
           'goat': 678,
           'pig': 1296,
           'cow': 3848,
           'sheep': 6769}
max_price = 0
max_animal = ''

for animal, price in animals.items():
    if money >= price >= max_price:
        max_price = price
        max_animal = animal

if max_price == 0:
    print(None)
else:
    quantity = money // max_price
    if quantity > 1:
        if max_animal == 'sheep':
            print(quantity, max_animal)
        else:
            print(quantity, max_animal + 's')
    else:
        print(quantity, max_animal)
