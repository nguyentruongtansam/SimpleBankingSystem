synthesis_index = float(input())
if synthesis_index < 2:
    print('Analytic')
elif synthesis_index <= 3:
    print('Synthetic')
else:
    print('Polysynthetic')
