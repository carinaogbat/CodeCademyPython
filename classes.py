#Instantiate a class:
class Facade:
  pass

facade_1 = Facade()

# Instantiation takes a class and turns it into an object, the type() function does the opposite of that. When called with an object, it returns the class that the object is an instance of.
# We then print out the type() of cool_instance and it shows us that this object is of type __main__.CoolClass.
# In Python __main__ means “this current file that we’re running” and so one could read the output from type() to mean “the class CoolClass that was defined here, in the script you’re currently running.”
class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)
#=><class '__main__.Facade'>

#adding class variables
class Grade:
  minimum_passing = 65

passing_grade = Grade()
print(passing_grade.minimum_passing)
#=> 65

#defining a method on a class
class Rules:

  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

#defining method with arguments on a cass
class Circle:
  pi = 3.14
  def area(self, radius):
    return self.pi * radius ** 2

circle = Circle()
pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)

# There are several methods that we can define in a Python class that have special behavior. These methods are sometimes 
# called “magic,” because they behave differently from regular methods. Another popular term is dunder methods, so-named 
# because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.

# The first dunder method we’re going to use is the __init__() method (note the two underscores before and after the 
# word “init”). This method is used to initialize a newly created object. It is called every time the class is 
# instantiated.

# Methods that are used to prepare an object being instantiated are called constructors. The word “constructor” is used 
# to describe similar features in other object-oriented programming languages but programmers who refer to a constructor
#  in Python are usually talking about the __init__() method.

class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:
 
      # then shout it out
      print(phrase.upper())
 
shout1 = Shouter("shout")
# prints "SHOUT"
 
shout2 = Shouter("shout")
# prints "SHOUT"
 
shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"

# Above we created a class called Shouter and every time we create an instance of Shouter the program prints out a shout.
#  Don’t worry, this doesn’t hurt the computer at all.

# Pay careful attention to the instantiation syntax we use. Shouter() looks a lot like a function call, doesn’t it? If 
# it’s a function, can we pass parameters to it? We absolutely can, and those parameters will be received by 
# the __init__() method.

#adding a constructor 
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")

teaching_table = Circle(36)

#### instance variables
# We’ve learned so far that a class is a schematic for a data type and an object is an instance of a class, but why 
# is there such a strong need to differentiate the two if each object can only have the methods and class variables 
# the class has? This is because each instance of a class can hold different kinds of data.

# The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances
#  of a class — they are variables that are specific to the object they are attached to.

# Let’s say that we have the following class definition:

class FakeDict:
  pass
# We can instantiate two different objects from this class, fake_dict1 and fake_dict2, and assign instance variables 
# to these objects using the same attribute notation that was used for accessing class variables.

fake_dict1 = FakeDict()
fake_dict2 = FakeDict()
 
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"

class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

### ATTRIBUTE FUNCTIONS ####
# Instance variables and class variables are both accessed similarly in Python. This is no mistake, they are both 
# considered attributes of an object. If we attempt to access an attribute that is neither a class variable nor an 
# instance variable of the object Python will throw an AttributeError.

# What if we aren’t sure if an object has an attribute or not? hasattr() will return True if an object has a given
#  attribute and False otherwise. If we want to get the actual value of the attribute, getattr() is a Python function
#   that will return the value of a given object and attribute. In this function, we can also supply a third argument
#    that will be the default if the object does not have the given attribute.

# The syntax and parameters for these functions look like this:

# hasattr(object, “attribute”) has two parameters:

# object : the object we are testing to see if it has a certain attribute
# attribute : name of attribute we want to see if it exists
# getattr(object, “attribute”, default) has three parameters (one of which is optional):

# object : the object whose attribute we want to evaluate
# attribute : name of attribute we want to evaluate
# default : the value that is returned if the attribute does not exist (note: this parameter is optional)

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for item in can_we_count_it:
  if hasattr(item, "count"):
    print(str(type(item)) + " has the count attribute")
  else:
    print(str(type(item)) + " does not have the count attribute")

#=> 
# Output:
# <class 'dict'> does not have the count attribute
# <class 'str'> has the count attribute
# <class 'int'> does not have the count attribute
# <class 'list'> has the count attribute