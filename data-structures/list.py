'''
List is basically a data structure which stores a group of objects or collections of different objects.
List are ordered, changeable, and can have duplicate elements.
Ordered 
Every element in the list have specific order or position
Note this order can be changed by some list method generally order remains the same.

Changeable (Mutable)
List are mutable it can be changed by some list method
New elements can be added or removed and existing elements in the list can be modified by some list method

Duplicate:-
List can have duplicate elements
'''
even_numbers = [2,4,6,8,10,12,14,16] 
odd_numbers  = [1,3,5,7,9,11,13,15]

list_of_data = ['a', 'b', 'c', 'd', 'e',1,2,3,4,5,6,"Green","Yellow","Blue","Red",False,True]
print(list_of_data)
print(even_numbers)
#Ordered
print(even_numbers[2]) #It will also print 6 if the order is not change explicitly.
#Changeable
list_of_data.pop(0)
list_of_data[2] = 'Hello'
list_of_data.append("Black")
print(list_of_data) #list_of_data has been manipulated!
print("\n")


# Accessing the list elements
# indexing starts from 0 to len(list)-1
# indexing can also be negative where last element starts from -1 ,-2,-3, and so on but if len()-no is < 0 then it will give IndexError(list index out of range)
print(list_of_data[2],even_numbers[-1],odd_numbers[-3],list_of_data[-4])
print("\n")

#Iterating throught the list elements
for data in list_of_data:
    print(data,end=" ")

print()
index = 0
while index < len(list_of_data):
    print(list_of_data[index],end=" ")
    index += 1
print("\n")
# List Methods
new_list = []
'''
1.) append
append method adds a new element/object to the end of the list
'''
new_list.append(1)
new_list.append(2)
new_list.append(3)
print(new_list)
new_list.append([4,5,6])
print(new_list) # if any other object is passed may be a list then it will add it into the last index.

'''
2.) extend
extend method add all the elements from the argument list or any iterable(tuple,string,etc) to end of the list
'''
new_list.pop()
new_list.extend([4,5,6,7])
print(new_list)

'''
3.) insert
insert method add a new element on the given index apart from last index.
'''
new_list.insert(2,"hello")
print(new_list)


'''
4.) index
index method returns the index of the first matched element
If the element is not found it will return ValueError.
'''
data_index = new_list.index("hello")
print(new_list,data_index)

'''
5.) clear 
clears all the element from the list

6.) pop
pop method removes element at the specified position. default is last index.
If index is invalid gives IndexError.

7.) remove
remove method removes the first matched element from the list.
If the element is not found it will return ValueError.
list_of_data.remove(4)

8.) count
returns the count of the element in the list if not found gives 0.

9.) reverse()
reverse the order of the list

10. sort
    list.sort(reverse=True|False, key=myFunc)
reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
key	Optional. A function to specify the sorting criteria(s)

'''
print("\n")

'''
Slicing.....
some_list[start:end:step] here end is not inclusive.
step can be negative the order would be changed.
'''
sliced_list = new_list[1:5]
print(sliced_list)
print("\n")
'''
new_list[1:] it prints from 1st index to the end.
new_list[:5] it prints from 1st index to 4th.
new_list[:] it gives the entire list.
new_list[1::2] it print from 1st index to the end but with a step of 5.
new_list[1:3] = [1,2,3] modifying the part of list.
if new_list = [1,2,3,4,5]
new_list[1:3] = ['a','b','c']
new_list -> [1,a,b,c,4,5]
'''

'''
List Comprehension....
[_ for _ in list if condition]
[_ if condition else _ for _ in list]
'''
data = [1,2,3,4,5,6,7,8]
print([num if num%2==0 else num/2 for num in data])
print([num**2 for num in data])

'''
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
multi-dimensional list comprehension
[[print(num) for num in data] for data in nested_list]
'''
_2d_list = [['O' if data%2==0 else 'X' for data in range(0,3)] for val in range(0,3)]
print(_2d_list)