#Objected oriented programming is a means of structuring programs so that the properties and behaviors are bundled into individual objects.
#Input -> Process -> Object
#for example translating European floor levels in an elevator (lift) to the US equivalent.
'''
inp = input("Europe Floor?: ")
usf = int(
    inp
) + 1  #This will translate the value of the European floor to the US floor, by adding 1 to the floor number asnd changing the string into an int
print("US Floor is: ", usf)  #This will print out the value.
'''
'''
- A program is made up of many cooperating objects.
- Each object represents a portion of the program and at the same time cooperates with the other working
objects
-A program is make of one or several objects working togther, as objects can make use
of each other's capabilities.
-An object is a bit of self-contained Code and data. Using the Object approach entails breaking the problem 
into smaller more understandable parts.
'''
'''
- A class defines the shape of an object, the data it contains, and code in it.
(in essence, the class is the template and the object is the product of the template or an instance of it)
- Methods live inside the class, and fields and attributes are the bits of data that define the class. 
'''
'''


class PartyAnimal:  #This is the template for making PartyAnimal objects
    x = 0  #Each PartyAnimal object has a bit of data.

    def party(self):  #Each partyAnimal object has a bit of code
        self.x = self.x + 2
        print(self.x)


an = PartyAnimal()  #Construct a PartyAnimal object and store in "an"
an.party()  #Tell the "an" object to run the party() code within it.
an.party()  #Tell the "an" object to run the party() code within it.
'''
'''

#The dir() command lists capabilities.
x = list()
type(x)
print(dir(x))
'''
'''
#These are use by Python itself.
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 

#This portion is the real operation that the object can perform
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
