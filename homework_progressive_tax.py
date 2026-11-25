salary = float(input('Hoghoogh salane (toman): '))
has_child = input('Aya farzand darid? (y/n): ') == 'y'

if salary <= 10_000_000:
    tax = 0
elif salary <= 25_000_000:
    tax = (salary - 10_000_000) * 0.10
else:
    tax = (25_000_000 - 10_000_000) * 0.10 + (salary - 25_000_000) * 0.20

if has_child:
    tax = tax - 500_000
    if tax < 0:
        tax = 0

print('Maliyat nahayi:', tax, 'toman')