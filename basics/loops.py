'''
Loops in Python
2 Types of Loops in Python
While Loop in Python
For Loop in Python
'''

# for i in object: 
'''
So here object can be any sequence type data type, iterator or string
'''
'''
 Here i will print numbers from 0 to 9 as range data type has range(start,end,step=1)
 Here end is exclusive.
 '''
for i in range(10):
    print(i,end=" ")
 
print("\n")   
L = [1,2,3,4,5]

# Tricky thing to explore ....
for i in L:
    print(i,L)
    L.pop(0)

'''
    While Loop in Python
'''

# while boolean_logic: here the loop will execute untill boolean_logic becomes False.

L = [1,2,3,4,5,6]
index = 0
while index < len(L):
    print(L[index],end="->")
    index += 1
    