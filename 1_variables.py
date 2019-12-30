import keyword
print(keyword.kwlist)
print("Total number of keywords", len(keyword.kwlist))

c = 'Hi Python'
print(type(c))
print('The text is -', c)

no_of_days = 365
no_of_hours = 24
print(no_of_days)
print(no_of_hours)

a, b, c = 5, 3.2, "Hey I love machine learning"  # assigning values in a single row
print(a, b, c)
print(a)
print(b)
print(c)

# This will return the datatype of the variable , allowed data types are Integer ,
print(type(a), type(b), type(c))

vFirst_Loca = 3
vSecond_Loca = 3
print(id(vFirst_Loca))
print(id(vSecond_Loca))
# as both the variables has same value , the memory location is also same.

x = 2
y = 3
z = x + y
print('Sum of X + y is :', z)

print('The location of X', id(x))
print(z)

# Multiline line messaging using triple coats
v_Message = """I have been working
for 12 years in IT"""
print(v_Message)

v_Message = 'Hello Python'
print('Length of my message is ', len(v_Message))
print('At Position 6 the letter we have is', v_Message[6])

v_Multi = 1+2+3 +\
    4+5+6 +\
    7+8
print('Multi Line Variable', v_Multi)
# Sum of numbers in multiple lines

v_First = 10
v_Second = 20
v_Third = 30
print('First Variable', v_First, 'Second Variable', v_Second, 'Third Variable', v_Third)

vFirst = 1 + 2j
print(vFirst, 'is a complex number ?')
print(isinstance(1+2j, complex))

# When we divide 2 integer values by defauly we will get float value in the output. To avoid float value we should use double slash.
a = x // y
print(a)

c = 9 ** 2  # Square of a number
print('Square is', c)

c = 9 ** 0.5  # Square root of a number
print('Square root is', c)

c = 5 % 3
print('Modules of a number is ', c)

d = 10
print(d == 10)  # Checking if the value is True or Not.

print('Float value is', float(10))
print('String Value is', str(20))
print('Integer Value is', int(100.56))

message = 'This is Sundeep '
print('Multiplication of a String ------', message * 20)

v_a = True
print(type(v_a))

vString = 'We are in ML class'
print(vString)
print(vString[0])
print(vString[-1])
print(vString[6:11])  # From 6 to 10 , 11th string will not be considered.
print(vString[:5])  # From 0 till 4th
print([vString[2:]])  # From position 2 till the end of the string

v_First = 1
v_Second = 'a'
print(str(v_First) + v_Second)
# Python Casting

my_String = 'This is my String'
print('Spliting of my String', my_String.split())
my_String1 = my_String.split()
print('1st Index Value of my String is', my_String1[1])

a = 'part one'  # Here a is 0
b = 1  # Here b is 1
c = 10  # Here c is 2
print("{2} {0} {1}".format(a, b, c))

v_message = 'Hello who are you "This is Sundeep"'
print(v_message)
print(type(v_message))

name = 'Mahesh'
print('Hello, %s!' % name)

name = 'Mahesh'
age = 23
print('%s is %d years old' % (name, age))

word = 'NagaKaliSundeep Maddu'
print(word.count('N'))
print(word.lower())
print(word.upper())
print('Capitalize --', word.capitalize())  # Only the first letter will be Captalized
print('Title --', word.title())  # First letter of every word will be capatalized
print(word.isupper())
print(word.islower())

v_String = 'Hello World! 123$'
print(v_String.endswith('3$'))
print('Whether my string Srates with Apple - ', v_String.startswith('Apple'))
print('Whether my string is alpha - ', v_String.isalpha())
print('Whether my string is digit - ', v_String.isdigit())
print(v_String.replace('123', '456'))
print('Strip Function', v_String.strip('123$'))
# print('List Function', v_String.list(v_String))

v_Var = 'Once Upon a time there is a Girl caled Appu - Appu is a CRAZY girl'
print('Finding Appu using rfind command', v_Var.rfind('Appu'))
print('Finding Appu using Index command', v_Var.index('Appu'))

vVar = 'Apple'
print(vVar.replace('App', 'Tuu'))

vVar = '$$$Andhra'
print(vVar.strip('$'))
print(vVar.split())
print(list(vVar))

vString = 'Once upon a time in India , There was a king called Tippu.India was a great country'
print(vString.rfind('India'))  # rfind will search from back , which means it start from -1
print(vString.index('India'))  # Index will search from front , which means this one start from 0

age = input("How old are you ?")
height = input("What is your Height")
weight = input("My Weight is")
print(f"So you are {age} old ,{height} feet tall , {weight} kilos heavy. ")

name = input("What is your name")
dish = input("What id your favorite dish")
print('Your name is {},of age{} from {} and you love{}'.format(name, age, city, dish))
