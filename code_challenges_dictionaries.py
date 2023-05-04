#QUESTION
# Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. 
# The function should return the sum of the values of the dictionary
#MY SOLUTION
# Write your sum_values function here:
def sum_values(my_dictionary):
  count = 0
  for item in my_dictionary.values():
    count += item
  return count
# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

#THEIR SOLUTION
def sum_values(my_dictionary):
  total = 0
  for value in my_dictionary.values():
    total += value
  return total

  #QUESTION
#   Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all 
#   integer keys and values, as a parameter. This function should return the sum of the values of
#    all even keys.
#MY SOLUTION

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  count = 0
  for key, value in my_dictionary.items():
    if key %2 == 0:
      count += value
  return count

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

#THEIR SOLUTION
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key%2 == 0:
      total += my_dictionary[key]
  return total

  #QUESTION
#   Create a function named add_ten that takes a dictionary with integer values named my_dictionary
#    as a parameter. The function should add 10 to every value in my_dictionary and return
#     my_dictionary

#MY SOLUTION
# Write your add_ten function here:
def add_ten(my_dictionary):
  for key, value in my_dictionary.items():
    my_dictionary[key] += 10
  return my_dictionary

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

#THEIR SOLUTION
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

#QUESTION
# Create a function named values_that_are_keys that takes a dictionary named my_dictionary as
#  a parameter. This function should return a list of all values in the dictionary that are
#   also keys.
#MY SOLUTION:
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  values_and_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      values_and_keys.append(value)
  return values_and_keys

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

#THEIR SOLUTION
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary:
      value_keys.append(value)
  return value_keys

  # For this solution, we iterate through every value within the dictionary. In order to check if
  #  it is also a key, we can use the in keyword. This checks the value against all of the keys
  #   in the dictionary to see if it exists as a key as well. If it does, then we append it to 
  #   our list of values which are also keys.