num1 = int(input('ingresar primer número '))
num2 = int(input('ingresar segundo número '))
num3 = int(input('ingresar tercer número'))

menor = min(num1, num2, num3)
mayor = max(num1, num2, num3)
media = (num1+num2+num3) - menor - mayor

if num1 !=num2:
    print('el numero medio es ',media)
elif num2 !=num3:
    print('el numero medio es ',media)
else:
    print('el número no existe ')