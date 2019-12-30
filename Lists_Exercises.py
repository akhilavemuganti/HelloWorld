#Sum all items in a list

list1 = [9,8,6,0,5,1]
print("Sum is: ",sum(list1))

sum = 0
for i in list1:
    sum = sum+i
print(sum)

#===================================================================================================================

#Multiplies all items

list1 =[3,5,7]
mul =1
for i in list1:
    mul = mul*i
print(mul)

#Largest number from the list
print(max(list1))

#Smallest number from the list
print(min(list1))

#
str = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in str:
    if(len(i)>1 and i[0] == i[-1]):
        count = count +1
        print(i)
print(count)

#=================================================================================================================

#7. Write a Python program to remove duplicates from a list
list1 = [10,20,30,10,40,60,30]

dup_items = set()
uniq_items = []
for x in list1:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
print(uniq_items)
#=================================================================================================================

#8. Write a Python program to check a list is empty or not.

list_m = []
list_n = [2,4,3,1,8,9]

if len(list_m)==0:
    print("list is empty")
else:
    print("List is not empty")
#==================================================================================================================

#9.Write a Python program to clone or copy a list
list_12 = [9,2,4,1,8,5,6]

list_13 = list_12.copy()
print(list_13)

#==================================================================================================================

# 11. Write a Python function that takes two lists and returns True if they have at least one common member.

def compare(l1,l2):
    result = False
    for i in list_a:
        for j in list_b:
            if i == j:
                result =True
                return result

list_a = [1,2,3,4,5]
list_b = [6,7,8,9,1]
print(compare(list_a,list_b))
#===================================================================================================================

#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
list_p = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color = [x for (i,x) in enumerate(list_p) if i not in (1,5)]
print(color)

#===================================================================================================================
#14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

list_c = [2,4,7,9,8,10,12,5,3]
list_update =[]
for item in list_c:
    if(item % 2 != 0):
        list_update.append(item)

print(list_update)

#==================================================================================================================
#15. Write a Python program to shuffle and print a specified list.
from random import shuffle
color = ['Red','Green','Yellow','Black']
shuffle(color)
print(color)
#=================================================================================================================

#16. Write a Python program to generate and print a list of first and last 5 elements where the values are
# square of numbers between 1 and 30 (both included).

l = list()
for i in range(1,31):
    l.append(i)
print(l)

new_list =[]
for item in l:
    new_list.append(item**2)
print(new_list[0:5])
print(new_list[-5:])
#==============================================================================================================

#17. Write a Python program to generate and print a list except for the first 5 elements, where the values
# are square of numbers between 1 and 30 (both included).
l = list()
for i in range(1,31):
    l.append(i)
print(l)

new_list =[]
for item in l:
    new_list.append(item**2)

print(new_list[5:])
#=================================================================================================================
#18. Write a Python program to generate all permutations of a list in Python.

import itertools
print(list(itertools.permutations([1,2,3])))

#=================================================================================================================
#19. Write a Python program to get the difference between the two lists
l1 =[2,3,5,6,7]
l2 =[2,3,9,8,5]

print(set(l2)-set(l1))
#=================================================================================================================

#20. Write a Python program access the index of a list.
l3 =[9,8,3,2,1,0]
for index,value in enumerate(l3):
    print(index,value)
#================================================================================================================

#21. Write a Python program to convert a list of characters into a string.
chars =['H','E','L','L','O',' ','W','O','R','L','D']
str1 = ''.join(chars)
print(str1)

#===============================================================================================================
#22. Write a Python program to find the index of an item in a specified list

l4 =[5,9,3,2,0,8]
print(l4.index(2))

#===============================================================================================================
#24. Write a Python program to append a list to the second list.

l1 = [2,3,4,8]
l2 = [1,0,5,9]

print(l1+l2)
#================================================================================================================
#25. Write a Python program to select an item randomly from a list.
import random
l4 =[9,0,3,7,8]
print(random.choice(l4))

#================================================================================================================
#27. Write a Python program to find the second smallest number in a list.

l3 = [0,9,2,4,1,7,11,17,10]
sec_min = min(l3)
print((sec_min))
for item in l3:
    if(item >min(l3) and item<sec_min):
        sec_min = item
print("Second min value: ",sec_min)


#================================================================================================================
#28. Write a Python program to find the second largest number in a list.

l3 = [9,2,4,1,7,11,17,98,45]
sec_max = max(l3)
print((sec_max))
for item in l3:
    if(item < max(l3)):
        sec_max = item
print("Second max value: ",sec_max)

#===============================================================================================================
#29. Write a Python program to get unique values from a list.

l =[9,4,2,5,3,2,9,1,0,10]

dup_items = set()
uniq_items = []
for x in l:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print("Unique list is ",uniq_items)
#==============================================================================================================
#30. Write a Python program to get the frequency of the elements in a list.
import collections

list =['Apple','Ball','Cat','Ball','Orange','Cat']
print(list)
count =collections.Counter(list)
print(count)


