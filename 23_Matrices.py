def validarInput(num):
    while num<=0:
        num=int(input('Valor Incorrecto, reinserte el valor'))
    return num
def crearMatriz(A,M,N):
    for i in range(M):
        fila=[]
        for j in range(N):
            fila.append(int(input('Inserte el valor del elemento')))
        A.append(fila)
    return A
def imprimirMatriz(matriz):
    for x in range(len(matriz)):
        print(matriz[x])
    return 0
def hallarMenor(fila):
    menor=fila[0]
    for i in range(len(fila)):
        if menor>fila[i]:
            menor=fila[i]
    return menor
def hallarMayor(fila):
    mayor=fila[0]
    for i in range(len(fila)):
        if fila[i]>mayor:
            mayor=fila[i]
    return mayor
def hallarRango(fila):
    rango=hallarMayor(fila)-hallarMenor(fila)
    return rango

M=int(input('Inserte el valor de M'))
M=validarInput(M)
N=int(input('Inserte el valor de N'))
N=validarInput(N)
A=[]
crearMatriz(A,M,N)
imprimirMatriz(A)
for x in range(M):
    mayor=hallarMayor(A[x])
    #Aca se hallan los datos antes que se inserten los nuevos elementos
    #para hallar los datos de la matriz antes de que se realicen los cambios
    menor=hallarMenor(A[x])
    rango=hallarRango(A[x])
    A[x].append(mayor)#Se insertan 3 elementos nuevos a cada fila
    A[x].append(menor)#Que al final eso termina siendo una columna nueva
    A[x].append(rango)
imprimirMatriz(A)        

