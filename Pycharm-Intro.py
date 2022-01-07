# Código de Python é executado linha por linha
# Definindo Strings (série de caracteres)
print("Rafael Dantas")
print('o----')
print(' ||||')
# Adicionando um operador
# Isso é uma expressão, elas produzem valor
print('*' * 10)

# Variáveis. Elas armazenam, temporariamente, um dado.
# Values: Integer != float != Boolean
price = 10
rating = 4.9
name = 'Rafael'
is_published = False
print(price)
# Exeercício: definir 3 variáveis para um paciente
full_name = 'John Smith'
age = 20
is_new = True

# Getting Input
name = input('What is your name? ')
print('Hi, ' + name)
# Exercício: extender o programa e perguntar duas perguntas.
# Nome da pessoa e cor favorita. Então printe uma mensagem "Rafa gosta de azul
name = input('What is your full name? ')
favorite_color = input('What is your favorite color? ')
print(name + ' likes ' + favorite_color)

# Type Conversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)
print(type(age))
print(str(age) + ' years old')
# Exercicio: pergunte o peso em libras e converta para quilos no terminal
weight_pounds = input('Weight (lbs): ')
weight_kilos = int(weight_pounds)/2.2046
#Quero a resposta arredondada e em kg
print(str(int(weight_kilos)),'Kg')

# Strings
course = "Python's Course for Beginners"
message = '''
Hi, IBM

Here is our first contact 

hope to be there soon,
Rafael.
'''
print (course)
print (message[5:8])
