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