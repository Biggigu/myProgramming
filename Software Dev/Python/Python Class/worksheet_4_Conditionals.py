import time
import os

#note
print("Warning!")
print("This is python worksheet 4 Conditionals")
print("There are 5 tasks in total.")


time.sleep(1)

input("Press Enter to start.")
os.system('cls')

#task 1

userNumber = int(input("Please enter a number: "))

if userNumber >= 1:
    print("The number is a Positive Number")
    
elif userNumber <= -1:
        print("The number is a Negative Number")
        
else:
        print("The number is Neutral")

time.sleep(1)

input("Press Enter to continue to Task 2")
os.system('cls')


# Task 2: Capital City Quiz
print("I will now ask you 6 questions about capital cities.")
print("For each correct answer, you will be awarded with 2 points.")
print("Let's get started!\n")

# Dictionary storing questions and correct answers
capitalCities = {
    "What is the capital city of USA?" : "Washington",
    "What is the capital city of Germany?" : "Berlin",
    "What is the capital city of Australia?" : "Canberra",
    "What is the capital city of Malta?" : "Valletta",
    "What is the capital city of Italy?" : "Rome",
    "What is the capital city of Spain?" : "Madrid"
}

# Initialize score
score = 0
perCorrectAnswer = 2  # Each correct answer is worth 2 points

# Ask questions and check answers
for question, correctAnswer in capitalCities.items():
    userInput = input(question + " ").strip().capitalize()  # Standardizing input

    if userInput == correctAnswer:
        print("✅ Correct!")
        score += perCorrectAnswer  # Add 2 points for a correct answer
    else:
        print(f"❌ Wrong! The correct answer is {correctAnswer}.")

    time.sleep(1)  # Short delay between questions

# After all questions, display final score message (NOW IT’S AT THE END)
print("\nQuiz Completed! 🎉 Your final score is:", score)

# Give feedback based on final score
if score == 12:
    print("🏆 Score! All answers were correct!")
elif score == 10:
    print("👏 You did very well! You made 1 mistake.")
elif score >= 8:
    print("👍 Well done! You know most capital cities.")
elif score >= 4:
    print("🙂 Not bad, but you can do better.")
else:
    print("😅 Better luck next time.")

time.sleep(1)
print("\nThanks for playing!")
os.system('cls')

#Task 3 
##Odd or even
print("This is the Odd or even python program.")

number == int(input("Please enter your number: "))

if number % 2 == 0:
    print("Your number is Even ✅")
else:
    print("Your number is Odd ❌")
    
#Task 4
##Age group: [1]Child, [2]Adult, [3] Pensioner
##Seating section [West A], [West C], [Millennium]
##Number of tickets

##Prices
##Category      WestA       WestC       Millennium
##  Child       10          10          5
##  Adult       20          20          12  
##Pensioner     