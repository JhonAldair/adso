num1 = int(input('ingrese un numero: '))

if num1>=0 and num1<=9:
    print('el numero tiene 1 cifra')
elif num1>=10 and num1<=99:
    print('el numero tiene dos cifras')
elif num1>=100 and num1<=999:
    print('el numero tiene tres cifras')
elif num>=1000 and num<=9999:
    print('el numero tiene 4 cifras')
else:
    print('el numero no es valido')