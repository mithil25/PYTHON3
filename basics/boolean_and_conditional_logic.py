# Boolean is a datatype which represents True or False

# Conditional Logic
'''
if some condition is True:
    execute this code
elif some condition is True:
    execute this code
else:
    execute this code
'''
country = 'India'
if country == 'India':
    print('India capital is Delhi')
elif country  == 'US':
    print('US capital is Washington DC')
else:
    print('Country List Not Added')
'''
Logical Operators
==  True if value of a is equal value of b
!=  True if value of a is not equal value of b
>   True if a > b else False
<   True if a < b else False
>=  True if a >= b else False
<=  True if a <= b else False
and or operator
if a is TRUE also b is TRUE then a and b result True else False
if a is False and b is False then a or b result False else True
not operator
if a is False then not a will be True
if a is True then not a will be False
'''    
'''
In python is and == are similar but they are totally different
== checks value for both of the operands
is check with if both operands point to the same memory location.
For small number from 0 to 255 and small string it uses interning mechanism to optimize memory allocation
So == and is results same for the above example.
'''