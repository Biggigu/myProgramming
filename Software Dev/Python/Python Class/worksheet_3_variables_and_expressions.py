import time
import os

#task 1
print("Warning!")
print("This is python worksheet 3 Variables and Expressions")
print("There are 7 tasks in total.")


time.sleep(3)

input("Press Enter to start.")
os.system('cls')

username = input("Whats your name? ")

userAge = int(input(username + " Please enter your age."))

import datetime

currentYear = datetime.date.today().year

dateBorn = currentYear - userAge

print(dateBorn)

print(f"{username}, you were born in {dateBorn}")


time.sleep(3)

input("Press Enter to continue to Task 2")
os.system('cls')


#task 2

specialOffer = int(0.85) #85%

totalBill = int(0) #0 ewro

studentOffer = totalBill - 45.00 #45 uro off per total bill

laptopPrice = int(input("Please input the cost price of the laptop here: "))

totalBill = laptopPrice * 0.85 - 45

print(f"Your total was {laptopPrice}, with Special Offer of 15% off and your Student Offer of 45.00 ewro off your Total is: {totalBill}")


time.sleep(3)

input("Press Enter to continue to Task 3")
os.system('cls')


#task3

userSMS = 650

aFreeSMS = 500

aSMS = 0.10

bSMS = 0.02

print(f"The user needs {userSMS} SMS per month")
print(f"Plan A you get {aFreeSMS} free SMS, the rest will cost {aSMS} each SMS")
print("Plan B you get 0 free SMS, the rest will cost 0.02")

print("The Cost of each plan will be: ")

planA = (userSMS - aFreeSMS) * aSMS

planB = userSMS * bSMS

print(f"Plan A will cost: {planA}, and planB will cost: {planB}")

time.sleep(3)

input("Press Enter to continue to Task 4")
os.system('cls')

#Task 4

yearlyMembA = 200 + (40.00 * 12)
yearlyMembB = 50 + (70 * 12)


print("A gym offers two type of memberships. The first membership has a €200 up-front fee and a €40 a monthly charge. The second membership has a €50 up-front fee and a €70 monthly charge.")

print(f"This means that per year Membership A will cost {yearlyMembA}")
print(f"While Membership B will cost {yearlyMembB}")

print("If a person will be a member at the gym for 10 years what would be the cost of each membership option?")

print(f"10 years of Membership A will cost {yearlyMembA *10} and Membership B will cost {yearlyMembB * 10}")

time.sleep(3)

input("Press Enter to continue to Task 5")
os.system('cls')

#task 5

coverBook = 25.00
discount = 0.6
shipping = 3.0
pages = 0.75

print("Hello, Welcome to the book store!")

print("The cover price of a book costs 25.00 euro.")

amountCoverBook = int(input("How many covers do you need?: "))
amountPages = int(input("Pages cost 0.75 euros each. How many pages do you need?: "))

print("Congratulations you have been given 40% Discount!")

bookstoreTotal = (amountCoverBook * coverBook) + (amountPages * pages)

print(f"Your total was: {bookstoreTotal}")
print(f"Applying Discount: {bookstoreTotal * discount}")
print(f"Applying Shipping: {shipping}")
print(f"Your New Total is: {(bookstoreTotal * discount + shipping)}")

time.sleep(3)

input("Press Enter to continue to Task 6")
os.system('cls')

#task 6

print("Welcome to the 3 word sentence program")

word1 = input("Please input word 1: ")
word2 = input("Please input word 2: ")
word3 = input("Please input word 3: ")

sentence = word1+ " " + word2+ " " + word3

print(f"Your 3 word sentence is: {sentence}")

#task 7

userFullName = input("Please whats your full name?: ")

repeatName = int(input("Give me a number ideally from 1 to 5: "))

print(f"Im going to repeat your full name for {repeatName} times.")

print((userFullName + " ")* repeatName)