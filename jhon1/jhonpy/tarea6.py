hora=int(input('ingrese la hora:'))
min=int(input('ingrese los minutos:'))
seg=int(input('ingrese los segundos:'))
seg=seg+1

if seg>=59:
    seg=0
    min=min+1
    if min>=59:
        min=0
        hora=hora+1
        if hora>23:
            hora=0
            print(hora,min,seg)

else:
    print('la hora es ',hora,min,seg)


