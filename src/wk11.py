# String manipulation

# Exercise 1:
target = input("Enter a string: ")
length = len(target)

print("It ends with a fullstop\n") if target[length - 1] == "." else print("It does not end with a fullstop\n")

pos = 0
for i in target:
    print(f"Position: {pos}: {i}")
    pos += 1


# Exercise 2:

string = input("Enter main text: ")
tofilter = input("Filter chars: ")

final = ""

for char in string:
    if char not in tofilter:
        final += char
print(f"Filtered: {final}")

# Exercise 3:

# Can be done with isupper and islower
def option_1():
    txt = input("Enter text: ")

    has_num = False
    has_alpha = False
    has_random = False
    all_uppercase = txt.isupper()
    all_lowercase = txt.islower()
    
    print(f"Length is {len(txt)}")
    for i in txt:
        if i.lower() in "abcdefghijklmnopqrstuvwxyz":
            has_alpha = True
        elif i in "0123456789":
            has_num = True
        else:
            has_random = True
    
        if has_num and has_alpha:
            break; 
    
    if has_random:
        print("", end="")
    elif has_num and has_alpha:
        print("Input is Aplhaneumeric")
    elif has_num: 
        print("Input is numerical")
    elif has_alpha:
        print("Input is Alphabetical")
    
    if all_uppercase and has_alpha:
        print("All alphabets are uppercase")
    elif all_lowercase and has_alpha:
        print("All Alphabers are lowercase")

def option_2():
    txt = input("Enter text")

    if txt.isalpha() and txt.isdigit():
        print("Input is alphanumeric")
    elif txt.isdigit():
        print("Input is numerical")
    elif txt.isalnum():
        print("Input is Aplhabetical")
    if txt.isupper() and not txt.isdigit():
        print("All letter(s) is uppercase")
    elif txt.islower() and not txt.isdigit():
        print("All letter(s) is lowercase")

# Exercise 4:

initial = text = input("Enter text: ")
length = len(text)

uppercount = 0
for char in text:
    uppercount +=1 if char.isupper() else 0
    if uppercount >= 2:
        text = text.upper()
        break

if length >= 10:
    if text.startswith("<<") and text.endswith(">>"):
        text = text.replace("<<", '""').replace(">>", '""')
    else:
        text += '**'
print(text)

# Exercise 5:

text = input("Enter text:")
print(f"Length is: {len(text)}")

try:
    val = int(text)
    print(f"Integer added 10: {val +10}")
except:
    try:
        val = float(text)
        print(f"Integer added 10: {val +10}")
    except:
        print("Invalid input")

# Exercise 6:

secret = "bee hive"
guessed = "--- ----"

while "-" in guessed:
    print(guessed)
    guess = input("Enter guess: ")
    if guess in secret:
        i = 0
        for char in secret.lower():
            if guess == char:
                guessed = guessed[:i] + char + guessed[i+1:]
            i += 1

print("You got it right!")

 
