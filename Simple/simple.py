import re
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

#Mathematic application
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
"""
'''
def cube(num):
    return num * num * num


print(cube(4))
'''
#Lists and linked lists.
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


'''
'''
--------------------------------------------------------------------------------------------------------------------------------------------------------------
llist = LinkedList()
llist.remove_node("a")
#Exception: List is empty

llist = LinkedList(["a", "b", "c", "d", "e"])
#a -> b -> c -> d -> e -> None

llist.remove_node("a")
#b -> c -> d -> e -> None

llist.remove_node("e")
#b -> c -> d -> None

llist.remove_node("c")
#b -> d -> None

llist.remove_node("a")
#Exception: Node with data 'a' not found
--------------------------------------------------------------------------------------------------------------------------------------------------------------
llist.add_before("a", Node("a"))
#Exception: List is empty

llist = LinkedList(["b", "c"])
#b -> c -> None

llist.add_before("b", Node("a"))

#a -> b -> c -> None

llist.add_before("b", Node("aa"))
llist.add_before("c", Node("bb"))

#a -> aa -> b -> bb -> c -> None

llist.add_before("n", Node("m"))
#Exception: Node with data 'n' not found
--------------------------------------------------------------------------------------------------------------------------------------------------------------
#the list is empty so we can't add a node to it
llist.add_after("a", Node("b"))
llist = LinkedList(["a", "b", "c", "d"])

llist.add_after("c", Node("cc"))
#In this case the list isnt empty, but we don't have an f node which will raise an Exception
llist.add_after("f", Node("g"))
print(llist)
--------------------------------------------------------------------------------------------------------------------------------------------------------------
llist = LinkedList(["a", "b", "c", "d"])
llist.add_last(Node("e"))
llist.add_last(Node("f"))
print(llist)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

llist.add_first(Node("b"))
llist.add_first(Node("a"))
llist = LinkedList(["a", "b", "c", "d", "e"])

for node in llist:
    print(node)
--------------------------------------------------------------------------------------------------------------------------------------------------------------

llist = LinkedList()
first_node = Node("a")
llist.head = first_node

second_node = Node("b")
third_node = Node("c")
first_node.next = second_node
second_node.next = third_node
print(llist)
--------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
#if statements.
'''

is_male = True
is_tall = False

if is_male or is_tall:
    print("Tall and male or both")
else:
    print("nor")

if is_male and is_tall:
    print("Tall and male")
else:
    print("neither")
'''

#if statements and comparisons.
'''
def max_num(x, y, z):
    if x >= y and x >= z:
        print("Max number is: ", x)
        return x
    elif y >= z and y >= x:
        print("Max number is: ", y)
        return y
    else:
        print("Max number is: ", z)
        return z


def min_num(x, y, z):
    if x <= y and x <= z:
        print("min number is: ", x)
        return x
    elif y <= z and y <= x:
        print("min number is: ", y)
        return y
    else:
        print("min number is: ", z)
        return z

max_num(99, 12, 43)
min_num(99,12,43)
'''
#Dictionaries (inside curly brackets) useful to store key value pairs.
'''
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Mar"])
print(monthConversions.get("Mid", "not a valid key"))
'''
#While loops
'''
i = 1

while i <= 10:
    print(i)
    i += 1
print("Done with loop")

'''
#For loops.
'''
tasks = ["code", "workout", "make food"]
for task in range(len(tasks)):
    print(tasks[task])

for letter in "Practice makes perfect":
print(letter)
'''
#exponent function.
'''
print(2**3)  #this is the simple way
#with the use of functions


def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    print(result)
    return result


raise_to_power(5, 2)
'''
#2D list.
'''

number_grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0]]

#The first squared brackets represents the rows, while the second square brackets represents the columns.
#print(number_grid[3][0])

for row in number_grid:
    for col in row:
        print(col)

'''

#Translator.
#This function will convert each vowel in the phrase to what ever letter we want it to
'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "M"

            else:

                translation = translation + "m"
        else:
            translation = translation + letter
    return translation


print(translate(input('Enter a phrase: ')))
'''
#Try and Except.
'''
try:
    #value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("invalid Input")
'''
#'''
#Reading from files.
#there are different modes in which to navigate the file.
#the "r" mode where you can read the file.
#the "w" mode where you can write into the file.
#the "a" mode where you can append into the file.
#and the "r+" mode where you can read and write on the file
#We can also have a count variable that will count the lines and print out the number of lines.
'''
employee_sheet = open("Simple\employees.txt", "r")
for i in employee_sheet:
    print(i)

search_in = open("Simple\employees.txt", "r")
for line in search_in:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)
'''
'''
count = 0
for line in employee_sheet:
    count = count + 1
    print("Line count: ", count)
employee_sheet.close()
'''
#'''
#Smallest value in an array.
'''

smallest = None
for value in [14, 21, 45, 2, 10, 23]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print(smallest, " Is the smallest value in the array")
'''

#Matching and Extracting Data
#re.search() returns a True/False depending on whether
#the string matches the regular expression.
#if we actually want the matching strings to be extracted, we use re.findall().
#we imported the re module at the top of this file.
'''
x = 'My 2 favourite numbers are 22 and 7'
y = re.findall('[0-9]+', x)
print(y)
'''
#this is to find the position of the '@', the service provider, and then print out the host of the email
'''
data = "From ryan@genericemail.com Thu Nov 10 14:25:23 2022"
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos + 1:sppos]
print(host)
'''

#The double split pattern. (Sometimes we split a line one way, and then grab one of the pieces) ->.
#of the line and split that piece again.
'''
data = "From ryan@genericemail.com Thu Nov 10 14:25:23 2022"
words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
'''

#The regex version
'''
lin = "From ryan@genericemail.com Thu Nov 10 14:25:23 2022"
y = re.findall('@([^ ]*)', lin)
print(y)
'''
#Spam confidence
hand
