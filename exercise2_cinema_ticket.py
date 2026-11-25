age = int(input('sen ra vared konid: '))

if age < 5:
    price = 0
elif age < 18:
    price = 50000
elif age <= 60:
    price = 100000
else:
    price = 70000

print('gheymat belit:', price, 'toman')