#calling variables in a print function and concatinating it with other variables.
"""
f_name, age = "Ryan", 21
is_male = True

#Print our original print function if it's specified that the user is male, otherwise print wrong user
if is_male is True:

    print("Hello I'm " + f_name + " and I'm " + str(age) + " years old")
else:
    print("wrong user")

#Selecting which part of the text we want to print
"""
"""
phrase = "Bottle of Water"
#this will select the index of the letter and print it
print(phrase[0])
#This will select the range of indices we want to print
print(phrase[0:7])
#This will replace the words/letters with a different ones
print(phrase.replace("Bottle", "Can"))

#taking user inputs
user_age = input("Please enter your age: ")
print("you are " + user_age + " years old!")
"""


#basic calculator.
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def times(x, y):
    return x * y


def divide(x, y):
    return x / y


print("+", "-", "*", "/")
while True:
    choice = input("select: ")

    if choice in ("+", "-", "*", "/"):
        num_1 = float(input("Please enter a digit: "))
        num_2 = float(input("Please enter a digit: "))
        if choice == "+":
            print(add(num_1, num_2))
        elif choice == "-":
            print(sub(num_1, num_2))
        elif choice == "*":
            print(times(num_1, num_2))
        elif choice == "/":
            print(divide(num_1, num_2))
        break
    else:
        print("Invalid choice")

