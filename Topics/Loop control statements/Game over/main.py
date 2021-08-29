scores = input().split()
# put your python code here
incorrect = 0
correct = 0
for score in scores:
    if score == 'I':
        incorrect += 1
        if incorrect == 3:
            break
    else:
        correct += 1
if incorrect == 3:
    print('Game over')
else:
    print('You won')
print(correct)
