tamaño=int(input("ingrese tamaño de cuadro mágico: "))

#valido que le tamaño de la matriz sea valido
while tamaño<3 or tamaño%2==0:
  print("tamaño invalido ", tamaño)
  tamaño=int(input("ingrese un número impar mayor que 1 : "))

print("tamaño valido para cuadro mágico: ", tamaño)
matriz=[]

#llenar con ceros la matriz
matriz=[[0 for i in range(tamaño)] for i in range(tamaño)]
#mostrar matriz con ceros
for dato in matriz:
  print(dato)

print("\nresultado:\n")
#calculando punto de inicio
fila=(int(tamaño/2-0.5))
columna=0

contador=1
columna_anterior=0
fila_anterior=0
while (contador<=tamaño*tamaño):
  matriz[fila][columna]=contador
  contador=contador+1
  #avanzar
  columna_anterior=columna
  fila_anterior=fila
  fila=fila-1
  columna=columna-1
  
  #validando si columna es negativa(por fuera de matriz)
  if columna<0:
    columna=tamaño-1
  #validando si fila es negativa(fuera de la matriz)
  if fila<0:
    fila=tamaño-1
  #se valida si la casilla esta ocupada
  if matriz[fila][columna]!=0:
    columna_anterior=columna_anterior+1
    columna=columna_anterior
    fila=fila_anterior
  #valida la posicion en cero,cero va a la derecha
  if columna==0 and fila==0 and matriz[0][0]!=0:
    columna=columna+1


#mostrar matriz modificada
for dato in matriz:
  print(dato)