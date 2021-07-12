age = int(input())

if age <= 16:
    print("Lion King")
elif age <= 25:
    print("Trainspotting")
elif age <= 40:
    print("Matrix")
else:
    print("Pulp Fiction" if age <= 60 else "Breakfast at Tiffany's")