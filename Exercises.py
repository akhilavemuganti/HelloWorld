#Exercises

#bdfbdv ncbgjfv cvbdggjb

"""
Exercise 1: Create a List of your favorite songs. Then create a list of your
favorite movies. Join the two lists together (Hint: List1 + List2). Finally,
append your favorite book to the end of the list and print it.
"""
listSongs=["song1","song2","song3","song4"]
listMovies=["movie1","movie2","movie3","movie4"]
print(listSongs)
print(listMovies)

newList=listSongs+listMovies
print(newList)

newList.append("Book1")
print(newList)
#----------------------------------------------------------------------------------------------------------
"""
Exercise 2: There were 20 people on a bus. 10 got off. 3 came on. 15
came on. 5 came off. If there were 3 more buses, and each had 15 people
throughout the bus ride, how many people were on all the buses at the last
stop? (Should be done via one equation in Python Shell)
"""
bus=20-10+3+15-5+(3*15)
print(bus)
#----------------------------------------------------------------------------------------------------------
"""
Exercise 3: Create a small program that will take in a User’s name and last
name (Hint: varName = input(“Enter your name”)), store both in two
variables. And then print out a message saying (“Hello there, FirstName
LastName”) (Using the %s symbols)
"""

firstName=input("Enter your first name")
lastName=input("Enter your last name")
print("Hello there %s"%firstName+" "+"%s"%lastName)
#----------------------------------------------------------------------------------------------------------

"""
Exercise 1: Create a loop that prints out either even numbers, or odd
numbers all the way up till your age. Ex: 2,4,6,….,14 
"""

for i in range(0,31):
    if(i%2==0):
        print(i)
##OR

for i in range(0,31,2):
    print(i)

#----------------------------------------------------------------------------------------------------------
"""
Exercise 2: Using if statements, create a variable called day, set it to
“Tuesday”. Check to see if day is equal to “Monday” or “Tuesday”, and if it
is, print, “Today is sunny”. If it is not, print “Today it will rain”
"""
day="Tuesday"
if(day=="Monday" or day=="Tuesday"):
    print("Today is sunny")
else:
    print("Today it will rain")

#----------------------------------------------------------------------------------------------------------
"""
Exercise 3: The weight of a person on the moon is 1/6th the weight of a
person standing on earth. Say that your weight on earth increases by 1 kg
every year. Write a program that will print your weight on the moon every
year for the next 10 years. (Your initial weight can be anything.)
"""

weightOnEarth=140
weightOnMoon=weightOnEarth*(1/6)
for i in range(1,11):
    weightOnMoon = weightOnEarth * (1 / 6)
    weightOnEarth = weightOnEarth + 1
    print("Weight on Earth %d" %weightOnEarth)
    print("Weight on Moon %d" %weightOnMoon)

#----------------------------------------------------------------------------------------------------------

