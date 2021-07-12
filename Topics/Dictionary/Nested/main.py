# please work with the variable children
# children = {'Emily': {'profession': 'artist', 'age': 5},
#             'Adam':
#                 {'profession': 'astronaut',
#                  'age': 9},
#             'Nancy':
#                 {'profession': 'programmer',
#                  'age': 14}}

children = {'Emily': 'artist', 'Adam': 'astronaut', 'Nancy': 'programmer'}
ages = {"Emily": 5, "Adam": 9, "Nancy": 14}

for child in children:
    children[child] = {"profession": children[child], "age": ages[child]}
