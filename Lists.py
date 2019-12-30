
# LISTS
shoplist = ['Apple','Mango','Banana','Carrot']
length = len(shoplist)
print('I have', len(shoplist), 'items to purchase.')
print('The items are ')
for item in shoplist:
    print(item)


shoplist.append('Rice')
print('The items appended: ')
for item in shoplist:
    print(item)


shoplist.insert(3,'Onion')
print('The items inserted: ')
for item in shoplist:
    print(item)

shoplist.sort(key=None, reverse=False)
print('The items are sorted: ')
for item in shoplist:
    print(item)

# =============================================================================================================#

my_list1 = [5,10,15,20,15,30]
print(my_list1)

my_list2 = ["Red","Blue","Green","Yellow"]
print(my_list2)

print("My Final List", my_list1+my_list2)

number = [6,7,8,9,1,0,13]
print(number[2]*5)

my_list2.append('Pink') #Add item to the list
my_list1.insert(3,8) #Insert at a given position
my_list2[3] = 'Purple' #Update an item at a given position
my_list2.remove('Red') #Remove a specified item
# my_list1.clear() #Clear the list

my_list1.extend(my_list2)
print(my_list1)

number.sort()  #Sorts  int  and float values
print(number)

print(my_list2.sort()) #Can't sort String

print(number.reverse())

sum_of_elements = sum(number)
print(sum_of_elements)


my_list1 = [5,10,15,20,15,30,2,6]
number = [6,7,8,9,1,0,13]

print("My_List1",my_list1)
print("Number",number)

element_wise_sum =[sum(pair) for pair in zip(my_list1,number)]
print(element_wise_sum)

print(my_list2)
sorted_by_second = sorted(my_list2,key=lambda el:el[1])
print(sorted_by_second)
sorted_by_both = sorted(my_list2,key=lambda el: (el[1],el[0]))
print(sorted_by_both)

list_of_chars = list('Apple')
print(list_of_chars)

new_list=['Apple','Ball','Cat','Apple','Orange','Apple']
print(new_list.count('Apple')) #Number of occurences of an element
print(new_list.index('Apple')) #Index of first occurence

#==============================================================================================================#

#Slicing a List

list1=['Blue','Green','Yellow','Burgandy','Orange']

sliced_List = list1[0:3]
print(sliced_List)

#Cut second item from the list
print(list1[1:2])
print(list1[1:-3])

#Cut second and third items from the list
print(list1[1:3])
print(list1[1:-2])

#Copy of original list
print(list1[:])

#Pop an item at the specified Index
list1.pop(1)
print(list1)

list2 = [9,7,22,8,66,21,75]
print("Max element ", max(list2))
print("Min element ", min(list2))

#=================================================================================================================#

#Nested Lists:

listx = [['Hello','World','Good','Morning'],[7,9,6,3,20,1,2],[7.8,9.6,8.6]]
print(listx[1][2]) #first index represents outer list, second represents the index of the item to print from sublist

listx.append(['Red', 'Green'])
print(listx)

#Update a value
listx[3][1] ='Yellow'
print(listx)

#===================================================================================================================

#Lists as Stacks LIFO

colors = ["Red","Yellow","Black"]
print(colors)
colors.append("Purple")
print(colors)
colors.append("Green")
print(colors)
colors.pop()
print(colors)

#=====================================================================================================================

#Lists as Queues FIFO

from collections import deque

color_list = deque(['red','blue','green','white'])
print(color_list)

color_list.append('Yellow')
color_list.append('Pink')
print(color_list)
color_list.popleft()
print(color_list)


