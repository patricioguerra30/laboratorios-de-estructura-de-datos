#PARTE 1
#EJERCICIO 1
import numpy as np
# def imprimir_par(n=2):
#     if n <= 100: 
#         print(n)  
#         imprimir_par(n + 2)  
# imprimir_par()  

# #EJERCICIO 2
# def suma_recursiva(n):
#     if n == 0:
#         return 0
#     else:
#         return n + suma_recursiva(n - 1)

# n = int(input("Ingrese un número: "))

# print("La suma de los números del 1 al", n, "es : ", suma_recursiva(n))

# #EJERCICIO 3

# def imprimir_piramide(n, current=1):
#     if current > n: 
#         return
#     print(' ' * (n - current) + ' '.join(str(i) for i in range(1, current + 1)))
#     imprimir_piramide(n, current + 1)

# n = int(input("Ingrese el número de niveles de la pirámide: "))
# imprimir_piramide(n)

# # #EJERCICIO 4

# def piramide_invert(n, current=1):
#    if current > n: 
#        return
#    print(' '.join(str(i) for i in range(current, 0, -1)))
#    piramide_invert(n, current + 1)

# n = int(input("Ingrese el número de niveles de la pirámide: "))
# piramide_invert(n)

# #EJERCICIO 5

# def imprimir_tabla_multiplicar(n, i=1):
#  if i > 12: 
#     return
#  print(f"{n} x {i} = {n * i}") 
#  imprimir_tabla_multiplicar(n, i + 1) 

# n = int(input("Ingrese un número: "))
# imprimir_tabla_multiplicar(n)

# #1Crear una matriz de números reales
# import numpy as np

# matriz_real = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(matriz_real)

# # 2Crear una matriz de números complejos
# matriz_compleja = np.array([[1+2j, 2+3j, 3+4j], [4+5j, 5+6j, 6+7j]])
# print(matriz_compleja)


# # 3 Crear una matriz de matrices

matriz_de_matrices = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(matriz_de_matrices)

# # 4 Acceder al elemento central de una matriz

# elemento_central = matriz_real[1, 1]
# print(elemento_central)

# # 5 Suma de dos matrices de diferentes tamaños

# matriz1 = np.array([[1, 2], [3, 4]])
# matriz2 = np.array([[5, 6], [7, 8]])
# suma_matrices = matriz1 + matriz2
# print(suma_matrices)

# # 6 Multiplicar una matriz por un número

# matriz_por_numero = matriz_real * 2
# print(matriz_por_numero)

# #7 Calcular la media de los elementos de una matriz
# media_valores = np.mean(matriz_real)
# print(media_valores)




# #PARTE 2
# #1 Cree una matriz de números aleatorios de tamaño 100x100:
# import numpy as np

# matriz_aleatoria = np.random.rand(100, 100)
# print("esta es la matriz",matriz_aleatoria)

# #2 Calcular la media de los elementos de la matriz
# media = np.mean(matriz_aleatoria)
# print("Media: ", media)

# mediana = np.median(matriz_aleatoria)
# print("Mediana: ", mediana)

# desviacion_estandar = np.std(matriz_aleatoria)
# print("Desviación estándar: ", desviacion_estandar)


# #3 Escribir una función que encuentre el elemento máximo de una matriz:
# def maximo(matriz):
#  return np.max(matriz)

# print("Elemento máximo: ", maximo(matriz_aleatoria))


# # 4 Escribir una función que encuentre la submatriz de mayor suma de una matriz:
# def submatriz_maxima(matriz):
#  fila, columna = matriz.shape
#  max_val = 0
#  max_submatriz = None

#  for i in range(fila):
#      for j in range(columna):
#          if i + 1 < fila and j + 1 < columna:
#              submatriz = matriz[i:i+2, j:j+2]
#              suma = np.sum(submatriz)
#              if suma > max_val:
#                max_val = suma
#                max_submatriz = submatriz
#  return max_submatriz

# print("Submatriz de mayor suma: \n", submatriz_maxima(matriz_aleatoria))

# # 5 Escribir una función que encuentre la matriz de covarianza de dos matrices:
# def matriz_covarianza(matriz1, matriz2):
#  return np.cov(matriz1, matriz2)

# matriz1 = np.random.rand(100, 100)
# matriz2 = np.random.rand(100, 100)

# print("Matriz de covarianza: \n", matriz_covarianza(matriz1, matriz2))