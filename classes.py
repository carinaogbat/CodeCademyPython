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