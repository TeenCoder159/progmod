# Practical 05 notes + answers:

# Exercise 1:
target = int(input("Enter number: "))

print("Add odd number(s):")
result = 0

for i in range(1, target+1, 2):
    print(f"\t{i}")
    result += i

print(f"Sum is {result}")

# Exercise 2:
num = -1
sum_of_nums = 0
while num != 0:
    num = int(input("Enter number: "))
    sum_of_nums += num
print(f"Sum is {sum_of_nums}")

# Exercise 3:

while True:
    try:
        cost = int(input("Enter the cost of item (S$): "))
        if cost < 0:
            print("Cost must be positive. Please re-enter")
            continue
        elif cost == 0:
            print("Program end")
            break
        else:
            print(f"The Selling price is {cost * 1.25}")
    except:
        print("Numerical values only. Please re-enter")

# Google colab link:

# Qsn 1a:

num_list = [2,5,9,7,8]
sum_val = 0

for val in num_list:
    sum_val += val ** 2

print(f"Total of squares in the list is: {sum_val}")

# Qsn 1b:

# Error prone code:
# print('Number','  ','Square')
# for num in [2,5,9,7,8]:
    # squarenum = num * num
    # total = total + (squarenum)
    # print(num, squarenum,sep='\t\t')
# print('Total of square in the list is',total)

# Error is total isnt defined (line 57 and line 59)

#Fixed code:
print('Number','  ','Square')

total = 0 # Only new line added

for num in [2,5,9,7,8]:
    squarenum = num * num
    total = total + (squarenum)
    print(num, squarenum,sep='\t\t')
print('Total of square in the list is',total)


# Qsn 2:
n = int(input("Enter a term of series: "))
val_sum = 0

if n >=2:
    for i in range(1, n+1):
        temp = "5" * i
        val_sum += int(temp)
        print(f"{temp}", sep=" ")
    print(f"Total sum is {val_sum}")
else:
    print("You must have at least 2 sets of numbers")



# Qsn 3:
total_sum = 0
student_count = int(input("Enter number of students: "))

for i in range(student_count):
    total_sum += float(input(f"Enter exam score for student {i+1}: ")) 

print(f"Average score = {total_sum / student_count:.2f}")

