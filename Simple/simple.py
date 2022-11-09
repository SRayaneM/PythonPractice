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
