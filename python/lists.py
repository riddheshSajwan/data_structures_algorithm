'''
values list in the argument of f doesn't get initialised everytime you call the function f, 
which means it keeps appending i to the previously obtained values list.
'''

def f(i,values=[]):
    
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)

'''
Output:
[1]
[1, 2]
[1, 2, 3]
'''


#############################################################################################

'''
fruit_list2 points to fruit_list1 location and 
fruit_list3 points to a new location that contains the list - ['Apple', 'Berry', 'Cherry', 'Papaya'] 
because slicing operation on fruit_list1 creates a list in new location

That's why, when fruit_list[0] is updated, it is an in-place operation.
'''

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
 
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
 
print(fruit_list1)
print(fruit_list2)
print(fruit_list3)
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
 
print(sum)

'''
Output:
['Guava', 'Berry', 'Cherry', 'Papaya']
['Guava', 'Berry', 'Cherry', 'Papaya']
['Apple', 'Kiwi', 'Cherry', 'Papaya']
22
'''