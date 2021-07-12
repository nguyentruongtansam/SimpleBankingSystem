income = int(input())
tax_percent = None
if 0 <= income <= 15_527:
    tax_percent = 0
elif 15_528 <= income <= 42707:
    tax_percent = 15
elif 42_708 <= income <= 132_406:
    tax_percent = 25
elif income >= 132_407:
    tax_percent = 28
calculated_tax = income * tax_percent / 100
print(f"The tax for {income} is {tax_percent}%. That is {calculated_tax:.0f} dollars!")
