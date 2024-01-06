'''
String is a text based data type .
In Python, strings are immutable. Once a string is created, its content cannot be changed. 
If you want to modify a string, you'll need to create a new one
This immutability provides certain advantages, including improved safety and simplicity in string handling.
It ensures that once a string is created, its content remains unchanged, preventing unintentional modifications. 
However, if you frequently need to modify a string, using a mutable data structure like a list and converting it back to a string might be a more suitable approach
'''
# Multiline String.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Note: in the result, the line breaks are inserted at the same position as in the code.

# Access individual characters of string as an array element

print(a[0],a[1])

#Slicing in the string
# -1 stands for end of string (len(string)-1), -2 len(string)-2
# str[start_index=0:end_index=-1:increment = 1] it will include from start_index to end_index-1 with increment as 
print(a[1:4])

# String Basic Methods
'''
UpperCase = upper()
LowerCase = lower()
Capitalize = capitalize()
Strip = strip(delimeter) # to remove whitespace or any delimiters
replace(target_string,string_to_replace)
split(delimeter,step) converts string into a list of strings based on delimiters.
'''
 
 