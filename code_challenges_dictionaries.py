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

#QUESTION
# Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
# The function should return the key associated with the largest value in the dictionary.
#MY SOLUTION
# Write your max_key function here:
def max_key(my_dictionary):
  largest_value = 0
  largest_key = "Carina"

  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key


# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

#THEIR SOLUTION
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

# In order to program the max algorithm using dictionaries, we need to keep track of the max value
#  and the key which is used to access it. We start by using float("-inf") in order to initialize 
#  them to the lowest possible value. To retrieve the key and value at the same time, we use the
#  items() function. Inside our loop, we overwrite the current largest value and the key used to
#   access whenever we find a larger value. We return the largest value’s key once we have iterated
#   through the entire dictionary.

#QUESTION
# Write a function named word_length_dictionary that takes a list of strings named words as a 
# parameter. The function should return a dictionary of key/value pairs where every key is a word
#  in words and every value is the length of that word.
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  word_dictionary = {}
  for word in words:
    word_dictionary[word] = len(word)
  return word_dictionary

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

#THEIR SOLUTION IS THE SAME AS ABOVE

#QUESTION
# Write a function named frequency_dictionary that takes a list of elements named words as a 
# parameter. The function should return a dictionary containing the frequency of each element 
# in words.
#MY SOLUTION
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  freq_dict = {}
  for word in words:
    if word not in freq_dict:
      freq_dict[word] = 0
    if word in freq_dict:
      freq_dict[word] += 1
  return freq_dict

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

#THEIR SOLUTION
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs

  # To create a new dictionary we set a variable equal to {}. We iterate through each of the 
  # strings in the list of strings and check if it is already in our dictionary using the in 
  # keyword. If it is not then we add it as a new key-value pair where the value is 0. Regardless
  #  of whether the string was already in the dictionary, increase the value by 1. This will 
  #  make it so all new entries will have a value of 1 and all existing entries will increase 
  #  their old value by 1.

  #QUESTION
  # Create a function named unique_values that takes a dictionary named my_dictionary as a 
  # parameter. The function should return the number of unique values in the dictionary.
  # Write your unique_values function here:
#MY SOLUTION
def unique_values(my_dictionary):
  unique_values = []
  for value in my_dictionary.values():
    if value not in unique_values:
      unique_values.append(value)
  return len(unique_values)
      

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1
#THEIR SOLUTION WAS THE SAME