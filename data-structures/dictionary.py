'''
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates
'''
carData  = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for  key, value in carData.items():
    print(key,value)

'''
To create a dictionary
user_info = {
    "user_id":"asdasd923ej12ne2e",
    "user_name":"mikey",
    "email":"mikey@gmai.com"
}
or user_info = dict(user_id="asdasd923ej12ne2e", user_name="mikey", email="mikey@gmai.com")
To get all keys from the dictionary
user.keys() returns dict_keys([key1,key2,....])
To get all values from the dictionary
user.values() returns dict_values([value1,value2,...])
To get all keys,values from the dictionary
user.items() returns dict_items([(key1,value1),(key2,value2),...])

Use in operator to check if particular key exists in the dictionary or not
'user_id' in user_info Returns True if key exists in the dictionary.
'mikey' in user_info Returns False as it is not key in the dictionary.
'''

'''
    Methods in dictionary
    
    clear() as the name suggests empty the dictionary.
    
    copy() returns  a copy of the dictionary copy and original has different memory location.
    
    fromkeys() returns a dictionary with the specified keys and the specified value.
    eg:- {}.fromkeys([key1,key2,...],"default_value")
    the first argument it will treat as iterable collection if string added then it will create default value for all the characters in the string.
    usually used to assing default values to the multiple keys in the dictionary.
    
    pop(key) removes the key from the dictionary. if the key is not in the dict it will throw KeyError exception.
    
    popitem() removes the last added key,value from the dictionary. if the dictionary is empty it will throw KeyError exception.
    
    update(dict) update method overrides and addeds arg dictionary into other dictionary if a = {1:"data"}
    and b = {2:"dataas"} so if a.update(b) then a will be {1:"data",2:"dataas"} ..    
'''


'''
    Dictionary Comprhension Example....
    {_:_ for _ in _}
    Conditional Logics with dictionary.
    {num:("even" if num%2==0 else "odd") for num in [1,2,3,4]}
'''
numbers = dict(first=1,second=2,third=3)
sq_numbers = {key:value**2 for key,value in numbers.items()}
print(numbers,sq_numbers)

