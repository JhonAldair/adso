x = int(input("Ingrese el valor del primer numero: "))
y = int(input("Ingrese el valor del segundo numero: "))

if (x<y):
    print('ascendente: ',x,'', '',y)
elif(x>y):
    print('descendente: ',x,', ',y)
else:
    print('Ambos valores son iguales')