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

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    self.circumference = 2 * self.pi * self.radius
    return self.circumference

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
#=>
# Creating circle with diameter 12
# Creating circle with diameter 36
# Creating circle with diameter 11460
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

#=>
# 37.68
# 113.04
# 35984.4

#Attributes can be added to user-defined objects after instantiation, so it’s possible for an object to have some 
# attributes that are not explicitly defined in an object’s constructor. We can use the dir() function to investigate
#  an object’s attributes at runtime. dir() is short for directory and offers an organized presentation of object 
# attributes. That’s certainly a lot more attributes than we defined! Python automatically adds a number of attributes
#  to all objects that get created. These internal attributes are usually indicated by double-underscores. But sure 
# enough, attribute is in that list.

# Do you remember being able to use type() on Python’s native data types? This is because they are also objects in 
# Python. Their classes are int, float, str, list, and dict. These Python classes have special syntax for their 
# instantiation, 1, 1.0, "hello", [], and {} specifically. But these instances are still full-blown objects to 
# Python

#EXAMPLE 
fun_list = [10, "string", {'abc': True}]
 
type(fun_list)
# Prints <class 'list'>
 
dir(fun_list)
# Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 
# 'remove', 'reverse', 'sort']
# print(dir(5))
#=>['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__',
#  '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', 
# '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__',
#  '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', 
# '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__',
#  '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', 
# '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
#  '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 
# 'numerator', 'real', 'to_bytes']
def this_function_is_an_object():
  pass

print(dir(this_function_is_an_object))
#=> ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', 
# '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__',
#  '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__',
#  '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__']

#We learned about the dunder method __init__(). Now, we will learn another dunder method called __repr__(). This is a method we can use to tell Python what we want the string representation of the class to be. __repr__() can only have one parameter, self, and must return a string.
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  # def __repr__(self):
  #   return f"Circle with radius {self.radius}"
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
print(medium_pizza)
print(teaching_table)
print(round_room)
#WITHOUT REPR
#=><__main__.Circle object at 0x7fe008b000f0>
# <__main__.Circle object at 0x7fe008b00080>
# <__main__.Circle object at 0x7fe008a9cc50>

#WITH REPR
#=> Circle with radius 6.0
# Circle with radius 18.0
# Circle with radius 5730.0

#REVIEW -- NOT COMPLETE WITH SUGGESTIONS
#you create a constructor by using the __init__ method
class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
  
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
    else:
      return
  def get_average(self):
    sum_of_grades = 0
    for grd in self.grades.score:
      sum_of_grades += grd
    number_of_grades = len(self.grades)
    return sum_of_grades / number_of_grades

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  def __init__(self, score):
    self.score = score
  minimum_passing = 65
  def is_passing(self):
    if self.score > 65:
      return "this is a passing grade"
    else:
      return "this is not a passing grade"


new_grade = Grade(100)
bad_grade = Grade(63)
pieter.add_grade(new_grade)
new_grade.is_passing()
print(new_grade.is_passing())
print(bad_grade.is_passing())
pieter.get_average()