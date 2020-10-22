vectorCredito=[0,0,0,0,0,0,0,0,0,0,0,0]
vectorDebito=[0,0,0,0,0,0,0,0,0,0,0,0]
contCredito=0
contDebito=0
mes=0
while mes!=13:
    mes=int(input('Inserte numero de mes,13 para salir:'))#Hallamos 3 variables y verificamos si el usuario introduce un valor invalido
    while mes<1 and mes>1:
        mes=int(input('valor invalido\n Inserte numero de mes, 13 para salir'))
    codigo=int(input('Inserte metodo de pago\n 1.Credito \n 2.Debito\n'))
    while codigo!=1 and codigo!=2:
        codigo=int(input('Valor Incorrecto\nInserte metodo de pago\n 1.Credito \n 2.Debito'))
    importe=int(input('Inserte el valor del importe'))
    while importe<=0:
            importe=int(input('valor incorrecto\nInserte el valor del importe'))
    if codigo==1 and mes!=13:
        vectorCredito[mes-1]+=importe
        contCredito+=1
    if codigo==2 and mes!=13:
        vectorDebito[mes-1]+=importe
        contDebito+=1
for x in range(12):
    print('Credito- Mes',x,': ',vectorCredito[x],'Debito- Mes',x,': ',vectorDebito[x])
