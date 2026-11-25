number = int(input('Yek adad sahih vared konid: '))

if number % 2 == 0:
    print('Adad zoj ast')
else:
    print('Adad fard ast')

if number > 0:
    print('Adad mosbat ast')
elif number < 0:
    print('Adad manfi ast')
else:
    print('Adad sefr ast')