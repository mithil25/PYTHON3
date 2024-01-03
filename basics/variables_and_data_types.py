''' 
Variable in python or any programming language is same as variable in Math
Variable are container that holds a value, they are basically named symbol that holds a data.
Data can be String, Number, Boolean, None etc..
Variable always assigned with variable name on left and value on right side.
Variable must be assigned before they can be used.
    
Variable can be assigned to other variable
for eg:-
''' 
x = 1
y = x
print(x, y)

''' 
Variable can be reassigned to another value.
for eg:- 
'''
x = 1 
x= 10
print(x, y)
''' 
We can assign multiple variable at same time 
    for eg: -
'''
x,y,z = 1,2,3
print(x, y, z) 
''' 
Variable Naming conventions
Variable name should start with a letter or underscore for eg:- _cat_name = 'kite', dog_name= 'moti' 1_x = 'asda' (Not Allowed) 
Result of variable name must consist number,letters and underscores _cat_name or dog_name mike@name = (Not Allowed)
Variable are case sensitive. For example cat and CAT are 2 different variable names
Global Variables
Global variables can be used by everyone, both inside of functions and outside.
'''
x = "awesome"
def myfunc():
    print("Python is " + x)

myfunc()
#    ----------------------------------------------------------------
def func():
        global x # (Uses x from global variables)
        x = "fantastic"

func()
print("Python is " + x)

'''
Data Type:-
Built-in Data Types
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
