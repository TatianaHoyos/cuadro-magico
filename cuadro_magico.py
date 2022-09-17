tamaño=int(input("ingrese tamaño de cuadro mágico "))

#valido que le tamaño de la matriz sea valido
while tamaño<3 or tamaño%2==0:
  print("tamaño invalido ", tamaño)
  tamaño=int(input("ingrese un número impar mayor que 1 : "))

print("tamaño valido para cuadro mágico: ", tamaño)
matriz=[]
lista=[]

#llenar con ceros la matriz
for conador in range(0,tamaño):
  lista.append(0)
  matriz.append(lista)
#se muestra la matrizz inicial
for  dato in matriz:
  print(dato)
