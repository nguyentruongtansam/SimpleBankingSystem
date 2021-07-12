units_number = int(input())
if units_number < 1:
    print('no army')
elif units_number <= 9:
    print('few')
elif units_number <= 49:
    print('pack')
elif units_number <= 499:
    print('horde')
elif units_number <= 999:
    print('swarm')
else:
    print('legion')
