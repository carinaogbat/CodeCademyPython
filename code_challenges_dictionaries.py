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