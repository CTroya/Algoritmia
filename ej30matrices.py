M=int(input('Inserte la cantidad de filas'))
N=int(input('Inserte la cantidad de columnas'))
matrix=[]
vector=[]
for i in range(M):#me falto validar m y n
    lista=[]
    for j in range(N):
        lista.append(input('Inserte el valor de los elementos'))
    matrix.append(lista)

for j in range(N-1):
    vector.append(matrix[0][j])
for i in range(M):
    vector.append(matrix[i][N-1])
for j in reversed(range(N-1)):
    vector.append(matrix[M-1][j])
for i in reversed(range(1,M-1)):
    vector.append(matrix[i][0])
for x in range(M):
    print(matrix[x])
print(vector)
