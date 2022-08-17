
# 1. Actualizar valores en diccionarios y listas
# 1. Cambia el valor 10 en x a 15 Una vez que hayas terminado, x ahora debería ser [5,2,3], [15,8,9] l.
# 2. Cambia el "apellido" del primer alumno de 'Jordan' a 'Bryant'.
# 3. En el directorio_deportes, cambia "Messi" por "Andrés".
# 4. Cambia el valor 20 en z a 30.

x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
estudiantes[0]['last_name'] = 'Bryant'
directorio_deportes['futbol'][0] = 'Andres'
z[0]['y'] = 30
print(x[1][0])
print(x)
print(estudiantes[0]['last_name'])
print(estudiantes)
print(directorio_deportes['futbol'][0])
print(directorio_deportes)
print(z[0]['y'])
print(z)

"""2. Iterar a través de una lista de diccionarios
    Crea una función iterateDictionary (some_list) para que, dada una lista de
    diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el
    valor asociado. Por ejemplo, dada la siguiente lista:"""

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def iterateDictionary(some_list):
    for index, item in enumerate(some_list):
        print(f"{some_list[index]}\n")

iterateDictionary(estudiantes)

"""3. Obtener valores de una lista de diccionarios
    Crea una función iterateDictionary2(key_name, some_list) que, dada una lista de
    diccionarios y un nombre de clave, la función imprima el valor almacenado en esa
    clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes)
    debería generar: Y iterateDictionary2('last _name', estudiantes) debería generar:"""

def iterateDictionary2(key_name, list):
    for x in list:
        print(x[key_name])
        
estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary2('first_name', estudiantes)
print("*" * 80)
iterateDictionary2('last_name', estudiantes) 

"""4. Iterar a través de un diccionarios con valores de lista
    Crea una función printInfo (some_dict) que, dado un diccionario cuyos valores son
    todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego
    imprima los valores asociados dentro de la lista del cada clave. Por ejemplo:"""

dojo = { 'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
        'instructores': ['Michale', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick','Minh', 'Devon']
        }

def printInfo(some_list):
    for x in (some_list):
        print(len(some_list[x])) #** imprime la longitud de la lista dentro del diccionario
        print(x.upper()) #** Imprime la mayuscula del primero
        for cityInstructores in (some_list[x]):
            print(cityInstructores) #** Imprime las ciudades e instructores en final
            
            
printInfo(dojo)

