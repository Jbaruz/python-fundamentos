num1 = 42 #Numbers
num2 = 2.3 #Float
boolean = True # Boolean
string = 'Hello World' #data types - string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit)) #Type check
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms') #list - add value
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2]) #string

if num1 > 45: #conditional
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:  ##conditional -lenght check
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):   #for loop
    print(x)
for x in range(2,5): 
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop() #delete value
pizza_toppings.pop(1) #delete value(1)

print(person)
person.pop('eye_color') #dictionary - delete value
print(person)

for topping in pizza_toppings: #for loop -start
    if topping == 'Pepperoni':
        continue #continue
    print('After 1st if statement')
    if topping == 'Olives':
        break #break

def print_hello_ten_times(): #function parameter
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): #function
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section #comment - multiple line
"""
""" Comments - single line
# print(num3) 
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
"""