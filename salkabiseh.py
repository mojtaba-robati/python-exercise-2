year = int(input('sal ra vared konid: '))

if year % 400 == 0:
    print('sal kabise ast')
elif year % 100 == 0:
    print('Sal kabise nist')
elif year % 4 == 0:
    print('Sal kabise ast')
else:
    print('Sal kabise nist')