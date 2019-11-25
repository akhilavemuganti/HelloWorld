
# LISTS
shoplist = ['Apple','Mango','Banana','Carrot']
length = len(shoplist)
print('I have ',  length, ' items to purchase')
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