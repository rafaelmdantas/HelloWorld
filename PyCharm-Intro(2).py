# Formated Strings
# Not the ideal strategy
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)
# Formated Strings helps visualization
msg = f'{first} [{last}] is a coder'
print (msg)

# String Methods
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.lower())
print(course)
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('python' in course)
# What was learned:
# len() function that counts the numbers of characteres in a str - general function in python
# Specific functions(methods): .upper();.lowe(); .title(); .find(); .replace(); in operator '...' in str

# Arithmetic Operator
print(10 * 3, 10//3, 10 % 3, 10 ** 3)
x= 10
# x = x + 3 whit augmented assignment(shorter form) is:
x += 3
print (x)

# Operator Precedence
# Parenthesis; Exponential 2 ** 3; Multiplication or division; addition or subtraction;
x = (10 + 3) * 2 ** 2
print(x)

# Math Functions
x = 2.9
print(round(x))
print(abs(-2.9))
import math
print(math.ceil(2.9))
print(math.floor(2.9))

# If Statements
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
   print("It's a lovely day")

print("Enjoy your day")
# Exercise: Price of a house is $1M.
            #If buyer has good credit,
                #they need to put down 10%
            #Otherwise
                #they nedd to put down 20%
            #Print the down payment
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")

# Logical Operators
# if applicant has high income AND good credit
    # Eligible for loan
has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

 # if applicant has high income OR good credit
    # Eligible for loan
has_high_income = False
has_good_credit = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

# if applicant has high income OR good credit
    # Eligible for loan
    #if applicant has good credit AND dosen't have a criminal record
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

# Comparison Operators
# if temperature is greater than 30
    # it's a hot day
# otherwise if it's less than 10
    # it's a cold day
# otherwise
    # it's neither hot nor cold
temperature = 30

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# if name is less than 3 characteres long
    #name must be at least 3 characters
# otherwise if it's more than 50 characters long
    #name can be a maximum of 50 characters
# otherwise
    #name looks good!
name = "Rafael"

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good")

# While Loops
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print("Done")











