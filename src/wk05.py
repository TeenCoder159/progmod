# Decision control structures:

# Exercise 1:

grade = input(
    "Enter grade: "
).lower()  # Simplify checking to only check lowercase letters
if grade == "a":
    print("GPA is 4.0")
elif grade == "b":
    print("GPA is 3.0")
elif grade == "c":
    print("GPA is 2.0")
elif grade == "d":
    print("GPA is: 1.0")
else:
    print("Invalid input")


# Exercise 2:

weight = int(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))

bmi = weight / (height**2)

# print("Your BMI is " + str(bmi))
# print("Your BMI is", bmi)
# Both methods work, but fstring is better

print(f"Your BMI is {bmi:.2f}")

if bmi >= 27.5:
    print("You are Obese")
elif bmi >= 23:
    print("You are Overweight")
elif bmi >= 18.5:
    print("You are Normal")
else:
    print("You are Underweight")

# Exercise 3:
try:
    acc_weight = int(input("Enter your weight in kg: "))
    height = float(input("Enter your height in m: "))
except:
    print("Invalid input detected, Exiting program")
else:
    min_weight = 18.5 * (height**2)
    max_weight = 22.9 * (height**2)

    print(f"Your ideal weight is between {min_weight:.2f} and {max_weight:.2f}")
    if weight >= min_weight and weight <= max_weight:
        print("Good Job, your weight is ideal!")
    else:
        print("Work harder to maintain and ideal weight")

# Exercise 4:

age = int(input("Enter your age: "))
day = int(input("Enter day of the week (1-7): "))

if 4 <= age <= 130:
    ticket_price = 9.0
    if day <= 5:
        if age < 16:
            ticket_price = 7.5
        elif age < 65:
            ticket_price = 10.0
        else:
            ticket_price = 5.5

    print(f"Ticket price: ${ticket_price:.2f}")
else:
    print("Invalid age")


# https://colab.research.google.com/drive/15aHTuKylGDSAUN32siF0WPAGu7iiGH3G#scrollTo=JT5LR2XhLgOS

# Question 1 (google colab until it says Exercise)

hours = int(input("Enter hours: "))
rate = float(input("Enter hourly rate: "))

pay = 0

if hours > 40:
    pay = 40 * rate
    pay += (hours - 40) * (rate * 1.5)
else:
    pay = hours * rate

print(f"Please pay: ${pay:.2f}")

# Question 2 (google colab):

age = int(input("Enter your age: "))

if age <= 6:
    print("Always follow your parents!")
elif age <= 20:
    print("Listen to your parents!")
else:
    print("You're an adult now. Behave responsibly")

# Question 3:

day = int(input("Enter day: "))

if 0 < day <= 7:
    if day <= 5:
        print("Please pay $5")
    else:
        age = int(input("Enter age: "))
        if age <= 5:
            print("Please pay $14")
        else:
            print("Please pay $28")
else:
    print("Invalid day")
