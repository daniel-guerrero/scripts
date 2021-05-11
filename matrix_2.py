# Este programa es para calcular determinates
from copy import deepcopy

def presentacion():
    print("\n*****************************************************************")
    print("*Matrix_2 es una aplicacion para calcular el determinanate de *\n"
          "*una matriz sin importar su tamaño                              *")
    print("\n****************************************************************\n")


presentacion()
print("\n")


fila = int(input("Ingrese en numero de filas:  "))
columna = int(input("Ingrese en numero de columnas:  "))

# con la funcion orden_m verificamos si la matriz es regular
def orden_m(fila, columna):
    filas = fila
    cols = columna
    if filas != cols:
        print("matrix no regular")
        exit(0)
    return (filas, cols)


def cuadrada(fila, columna):
    filas, columnas = orden_m(fila, columna)
    if (filas == columnas):
        print("La matriz es cuadrada")
    else:
        print("la matriz no es cuadrada")
        exit(0)

#con la funcion agregar_elem, agregamos filas y columnas a la matriz
def agregar_elem(fila, columna):
    matriz = []
    for k in range(fila):
        matriz.append([0]*columna)
    for i in range(fila):
        for j in range(columna):
            matriz[i][j] = int(input("elemento de la matriz :  "))
    return (matriz)

matrix = agregar_elem(fila, columna)

def det_1(matrix ,fila, columna):
    filas, columnas = orden_m(fila, columna)
    if (filas==1) and (columnas==1):
        return (f"Determiante 1*1, valor del determinante:", abs(filas))
    else:
        print("Esta matriz no es 1*1")
        exit(0)

#esta funcion pequeña_matrix es para reducir la matriz.

def reduccion_matrix(original_matrix, row, column):
    new_matrix = deepcopy(original_matrix)
    new_matrix.remove(original_matrix[row])
    for i in range(len(new_matrix)):
        new_matrix[i].remove(new_matrix[i][column])
    return new_matrix

#en esta funcion determinante_nxn, se encarga de resolver todos los determinantes
def determinante_nxn(matrix):
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            return orden_m(fila, columna)
    if len(matrix) == 1:
        return det_1(matrix, fila, columna)
    elif len(matrix) == 2:
        simple_determinant = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        return simple_determinant
    else:
        res = 0
        num_columns = num_rows
        for j in range(num_columns):
            cofactor = (-1)**(0+j) * matrix[0][j] * determinante_nxn(reduccion_matrix(matrix,0,j))
            res += cofactor
    return res



print(determinante_nxn(matrix))

# para ejecutar este programa se debe colocar en la consola python matrix_2.py
