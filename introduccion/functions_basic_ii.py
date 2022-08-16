"""1. Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve

una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta
0 (como último elemento).
o Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]"""


def countdown(num):
    list = []
    for x in range(0,num+1):
        list.insert(0,x)
    return list
print(countdown(5))

"""2. Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime
    el primer valor y devuelve el segundo.
    0 Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2"""
a = 1
b = 2
def xyz(a,b):
    print(a)
    return b
xyz(a,b)
print(b)

"""3. Primero más longitud: crea una función que acepte una lista y devuelva la suma del
    primer valor de la lista, más la longitud de la lista.
    O Ejemplo: primero_mas _longitud([1,2,3,4,5]) debe devolver 6 (primer valor: +length: 5)"""
list = [1,2,3,4,5]
def xyz(list):
    sumaList = list[0]+ len(list)
    print(sumaList)
xyz(list)

"""4. Valores mayores que el segundo: escribe una función que acepte una lista y cree una
    nueva que contenga solo los valores de la lista original que sean mayores que su
    segundo valor. Imprime cuántos valores son luego devuelve la lista nueva. Si la lista
    tiene menos de 2 elementos, has que la función devuelva False
    • Ejemplo: valores_mayores_que_el_segundo((5,2,3,2,1,4]) debe imprimir 3 y
    devolver 5,3,4]
    Ejemplo: valores _mayores_que_el_segundo([3]) debe devolver False"""

initialList = [5,2,3,2,1,4]

def x(list):
    if(len(list) < 2):
        return False
    finalList = []
    second_value = list[1]
    for num in list:
        if num > second_value:
            finalList.append(num)
    return finalList
result = x(initialList)
print(initialList[2])
print(result)

"""5. Esta longitud, ese valor: escribe una función que acepte dos enteros como
    parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud
    sea igual al tamaño dado, y cuyos valores sean todos el valor dado.
    O Ejemplo: length_and _value (4,7) debe devolver [7,7,7,7]

    Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2)"""

size = 6
value = 2
def length_value(size,value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list
result = length_value(size,value)
print(result)