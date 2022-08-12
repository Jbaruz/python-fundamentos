# 1. Básico: imprime todos los números enteros del 0 al 0 150.
for x in range(0,151):
    print(x)

# 2. Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.

for z in range (0, 1001, 5):
    print(z)

""" 3. Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5,
imprime "Coding" en su lugar. Si es divisible por 10, imprime "Coding Dojo."""
for x in range(0,101):
    if x % 5 ==0:
        print(x)
        print("Coding")
        print("*"*65)
    if x % 10 ==0:
        print(x)
        print("Coding Dojo")
        
# 4. Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
sum = 0
for num in range (0,500000):
    if not num % 2 == 0:
        sum += num
print(sum)

# 5 Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for num4 in range (2018, 0, -4):
    print(num4)

"""6. Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en
lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult.
Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas
sucesivas)."""
lowNum = 2
highNum = 9
mult = 3

for integer in range(lowNum, highNum+1):
    if integer % mult == 0:
        lowNum += integer
        print(integer)