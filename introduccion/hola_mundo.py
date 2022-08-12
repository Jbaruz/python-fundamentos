# 1. TAREA: imprime "Hola, mundo"
print("Hola mundo" )
# 2. imprime "Hola, Juan" con el nombre en una variable
name = "Juan"
print( "Hola" , "Juan")	# con una coma
print("Hola" + name)	# con un +
# 3. imprimir "Hola 42!" con el número en una variable
name = 11
print("hola" , 11)	# con una coma
print("hola" + str(11))	# con una +	-- este debería arrojar un error
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "Sudado de pescado"
fave_food2 = "Udon Soap"
print("Amo comer {} y {}" .format(fave_food1, fave_food2)) # con .format()
print(f"Amo comer {fave_food1} y {fave_food2}") # con una cadena f

