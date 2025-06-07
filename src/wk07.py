# Exercise 1:

total_cr = 0
total_cp = 0

for i in range(1,6):
    print(f"LU {i}")
    
    score = int(input("Enter score for LU: "))
    cr = int(input("Enter Credit for LU: "))

    if score >= 80:
        total_cp += (cr * 4.0)
    elif score >= 75:
        total_cp += (cr * 3.5)
    elif score >= 70:
        total_cp += (cr * 3.0)
    elif score >= 65:
        total_cp += (cr * 2.5)
    elif score >= 60:
        total_cp += (cr * 2.0)
    elif score >= 55:
        total_cp += (cr * 1.5)
    elif score >= 50:
        total_cp += (cr * 1.0)
    # Else not needed as we will end up adding a 0 to total_cp, which is unneccesarry
    
    total_cr += cr

print(f"Your GPA for 5 LU is {total_cp / total_cr:.2f}")


# Exercise 2:

# Printing the pyramid kinda thing
height = int(input("Enter height; "))
for row in range(1, height+1):
    for num in range(1, row+1):
        print(num, end=" ")
    print()

# Exercise 3:
student_count = int(input("Enter number of students: "))
test_count = int(input("Enter number of test: "))

for student in range(student_count):
    total_test = 0
    print(f"******* Student #{student+1} *******")
    for test in range(test_count):
        total_test += int(input(f"Test {test+1} score: "))

    print(f"Average score for student {student+1} is {total_test / test_count}")


# Exercise 4:
# Prime numbers thing

max = int(input("Enter the max number: "))
print(f"\nPrime numbers before {max}:")
for num in range(2, max+1):
    # All the numbers till the max
    is_prime = True
    for num_below_target in range(2, num):
        # all nums in the sqrt of each num
        if num%num_below_target == 0: # If num can be divided by a number perfectly (AKA has a factor)
            is_prime = False


    if is_prime:
        print(num)


# Exercise 5:
# The annoying menu thing:

print("Menu\n===")

answer = "y"
tot_cost = 0.0
while answer.lower() == "y":
    print("Burger: 0\nDrink: 1")
    option = int(input("Enter your order: "))
    option = "Burger" if option == 0 else "Drink"

    for count in range(int(input(f"How many {option} for this order?: "))):
        tot_cost += float(input(f"Enter {option} {count+1} cost: "))
    print(f"Total cost is: {tot_cost:.2f}")

    answer = input("Would you like to continue? [y/n]: ")

print(f"\nThank you for shopping with us. Please pay: ${tot_cost:.2f}")

