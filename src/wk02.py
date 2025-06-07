# Exercise 1:

totalHour = 10.5
rate = 12.35 

pay = totalHour * rate

print(f"Total Hour = ${totalHour:.2f}\nHourly Rate = ${rate:.2f}\nSalary = ${pay:.2f}")

# Exercise 2:

working_hours = float(input("Total Working Hours: "))
hourly_rate = float(input("Hourly rate: "))
print(f"Salary is: {working_hours*hourly_rate:.2f}")

# Exercise 3:
# Screw debugger... read the code, add print statements and do it yourself you lazy bum.

# Exercise 4:
name = input("Enter name: ")
admin_no = input("Admin number: ")
age = int(input("Enter age: "))
gender = input("Enter gender (male / female): ") #.lower() is only for verifying if its a he or a she
weight = int(input("Enter weight: (kg): "))
height = float(input("Enter height (m): "))

print(f"Hi {name}\nYour admin number is {admin_no} and age is {age}\nYour gender is {gender} and bmi is {weight / (height ** 2):.2f}")

# Exercise 5:

# For loop solution (better one, but not what they wanted for this scenario)

score = 0 
for i in range(3):
    t_score = int(input(f"What is your score for Test {i+1}: "))
    weightage = int(input(f"Weightage for Test {i+1}: ")) / 100.0

    score += t_score * weightage
score += int(input("Final test score: ")) * 0.5
print(f"Your final score is {score}%")

# Exercise 6:

share_count = 2000
share_price = 0.4

sb_commission = 0.03
sale_commission = 0.02

current_stock_price = float(input("Enter current stock price (S$): "))
total_commission = (share_count * share_price * sb_commission) + (share_count * current_stock_price * sale_commission)
print(f"Total commission = {total_commission}")
print(f"Net profit / loss = {(share_count * current_stock_price) - (share_count * share_price) - total_commission}")

# Exercise 7:

import random

height = random.randint(1, 200)
print(f"Height {height}cm is {int(height/100)}m and {height % 100}")

# Exercise 8:

str_1 = input("Enter string 1: ")
str_2 = input("Enter string 2: ")

print(f"{str_1}\t{str_2}\n{str_2}\t{str_1}")





