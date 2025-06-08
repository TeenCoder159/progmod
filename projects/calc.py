try:
    num_1 = float(input("Enter num 1: "))
    num_2 = float(input("Enter num 2: "))
except:
    print("Invalid input. Error converting. Exiting Program")
else:
    operation = input("Enter operation: ")
    output = "Result is "
    if operation == "+":
        output += str(num_2 + num_1)
    elif operation == "-":
        output += str(num_1 - num_2)
    elif operation == "*" or operation == "x":
        output += str(num_1 * num_2)
    elif operation == "/":
        output += str(num_1 / num_2)
    elif operation == "**" or operation == "^":
        output += str(num_1**num_2)
    else:
        output = "Invalid input. Please enter a valid operation"

    print(output)


# Alternatively, use an eval() function but we don't talk about that
