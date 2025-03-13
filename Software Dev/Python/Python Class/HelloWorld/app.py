'''from datetime import datetime

print("Samuel Bartolo")
print('o----')
print(' ||||')
print(' *' * 4)

price = 10  #intiger
rating = 4.9 #float
name = 'Samuel'
is_published = True
print(price)

#   We check in a patient named John Smith,
#   He is 20 years olf and is a new patient.

#   Give me 3 variables for his name,
#   age and another variable to tell
#   if he is new or existing patient.

fullName = 'John Smith'
age = 20
is_new = True

## How to receive inputs from user

yourName = input('What is your name? ')
print ('Hi ' + yourName + '.')

# Ask 2 questions:
#               Person`s Name
#               Favourite Color.
# Then print a message like
# "name likes color"

yourNameA = input('Hey there what is your name? ')
print('Good to see you ' + yourNameA +'!')
favouriteColor = input('Tell me whats your Favourite Color ' + yourNameA + '? ')
print('WoW ' + favouriteColor + ' what a beautiful color ' + yourNameA + '!')

## Great Now we will continue by "Type Conversions"

birthYear = input('Birth year: ')
print(type(birthYear))
yourAge = 2024 - int(birthYear)
print(type(yourAge))
print(yourAge)

# Ask Users a Weight in Kilograms,
# Convert it to pounds

weight_kg = input("Weight (Kg): ")
weight_lbs = int(weight_kg) / 1.45
print(weight_lbs)

##Strings##
course = "Python's Course for Beginners"
print(course)

course_again = 'Python for "Beginners"'

course_again_again =
Hi John

Here is Our email to you.

Kind Regards,
The support Team


courseAgain = 'python for Beginners'
print('you can choose to print letters individually in python look ' + courseAgain[3] + courseAgain[14] + ' is the 3rd and 14th Letter')
print(courseAgain[0:5])

##Continue from  https://www.youtube.com/watch?v=_uQrJ0TkZlc at 36:00##

#Worksheet 4 task 1

userIn = int(input("Enter an integer: "))

if userIn > 0 :
    print("Positive number")
elif userIn < 0 :
    print("Negative Number")
else:
    print("Neutral")

mark = int(input("Enter a Valid Mark between 0 - 100"))
if 0 <= mark <=100:
    print("The mark is valid")
else:
    print("The mark is out of range")

#task 5

#worksheet5_task5
#the program has to read temperature in centigrade and display a suitable message according to the temperature states below
# Temp <0 is Freezing weather
# temp 0-10 is Very cold weather
# temp 10-20 is cold weather
# temp 20-30 normal weather
# temp 30-40 its hot
# temp 40 - 50 It's very hot



def determine_weather(currenTemp):
    if currenTemp < 0:
        return "Freezing weather"
    elif 0 <= currenTemp <= 10:
        return "Very cold weather"
    elif 10 < currenTemp <= 20:
        return "Cold weather"
    elif 20 < currenTemp <= 30:
        return "Normal weather"
    elif 30 < currenTemp <= 40:
        return "It's hot"
    elif 40 < currenTemp <= 50:
        return "It's very hot"
    else:
        return "Temperature out of range"

try:
    currentTemp = float(input("Enter the temperature in Celsius: "))
    print(determine_weather(currenTemp))
except ValueError:
    print("Please enter a valid number.")


#CPU EFFICIENCY Method

def determine_weather(temp):
    conditions = [
        (-float('inf'), 0, "Freezing weather"),
        (0, 10, "Very cold weather"),
        (10, 20, "Cold weather"),
        (20, 30, "Normal weather"),
        (30, 40, "It's hot"),
        (40, 50, "It's very hot"),
        (50, float('inf'), "Temperature out of range")
    ]

    for lower, upper, message in conditions:
        if lower <= temp <= upper:
            return message


try:
    temp = float(input("Enter the temperature in Celsius: "))
    print(determine_weather(temp))
except ValueError:
    print("Please enter a valid number.")

#
# python has 2 statements to create loops/iterations.repetition
#
# "while"     and      "for"
#
# for  is used when you know how many times to repeat
#
# while is used for when you don't know the amount if times the code needs to repeat
#
# because you depend on an external event
for i in range (5):
    print("Hello")

#this will print hello 5 times

for i in range(5):
    print(i)

#This will print 5 numbers from 0 to 4

for i in range (1,11):
    print(i)

#or

for i in range (10):
    print(i+1)

#same answer#

for i in rance (1,10):
    if i%2 == 1:
        print(1)

#ultimate answer
for i in range(1,10,2):
    print(i)
#result is 1,3,5,7,9

for i in range(10,-1,-1):
    print(i)

#so now let's do martin * 5

for i in range(1,6):
    print('*'*i)

for i in range(1,height +1):
    print(('*' * (2*i-1)).center(2* height -1))

#actual answer how the teacher expects me to do it
for i in range (1,10,2):
    text = '*'*i
    print(text.center(60))
    for i in range (5):
        print('*'*5)

for i in range (5):
    if i == 0 or i == 5 -1:
        print("*" + " " * 5)
    else:
        print("*" + " " * (5 -2) + "*")


#nah this is how it should be done ok?
 for i in range(5):
     if i == 0 or i == 5-1:
         print("*"*5)
     else:
         print("*" + " " * (5 -2) + "*")
'''
#while loop
# set counter
# check boolean
# modify counter#


#print numbers from 1 to 10 using while loop
counter = 1
while counter <=10:
    print(counter)
    counter = counter + 1