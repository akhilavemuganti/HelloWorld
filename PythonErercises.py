#Python Version
import sys
print(sys.version)
print("Version info.")
print (sys.version_info)
#==================================================================================================================

#Python Date Time
from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

#==================================================================================================================

#Python Circle Area

# print('Enter the radius:')
# r =float(input())
# area = 3.14*r*r
# print('Area is: ' + str(area))

#===================================================================================================================

print('Enter some numbers seperated by commas:')
values = input()
list1 = values.split(',')
tuple1 = tuple(list1)
print(list1)
print(tuple1)

#===================================================================================================================

#Write a Python program to sum all the items in a list.

l1=[5,7,3,4,8]
sum1 =0
for item in l1:
    sum1=sum1 + item
print(sum1)

#===================================================================================================================

#Write a Python program to multiplies all the items in a list.

l2 = [8,2,3]
mul = 1
for item in l2:
    mul =mul*item
print(mul)

#==================================================================================================================

#Unique values in a list

list1 = [10,20,40,30,20,50,40,80,30]
print("My original List: ")
print(list1)
uniqueList = list(set(list1))
print("Unique List: ")
print(uniqueList)

#==================================================================================================================

#Frequency of elements in a list

import collections

list1 = [10,10,10,20,20,30,40,40]
print("Original List: ", list1)
ctr = collections.Counter(list1)
print("Frequency of elements: ",ctr)

#===================================================================================================================

#Select a random number from the list
import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))