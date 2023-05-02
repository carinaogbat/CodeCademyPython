#***QUESTION
# Write a function called unique_english_letters that takes the string word as a parameter. 
# The function should return the total number of unique letters in the string. Uppercase and
#  lowercase letters should be counted as different letters.

# We’ve given you a list of every uppercase and lower case letter in the English alphabet.
#  It will be helpful to include that list in your function.

#***MY SOLUTION***
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  unique_letters = ''
  for letter in word:
    if letter in letters and letter not in unique_letters:
      unique_letters += letter
  return len(unique_letters)

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

#***THEIR SOLUTION***
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

#***QUESTION
# Write a function named count_char_x that takes a string named word and a single character 
# named x as parameters. The function should return the number of times x appears in word.

#   *** MY SOLUTION ***

# Write your count_char_x function here:
def count_char_x(word, x):
  count = 0
  for char in word:
    if char == x:
      count += 1
  return count


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1


# *** QUESTION ***
# Write a function named substring_between_letters that takes a string named word, a 
# single character named start, and another character named end. This function should 
# return the substring between the first occurrence of start and end in word. If start 
# or end are not in word, the function should return word.
# For example, substring_between_letters("apple", "p", "e") should return "pl".

#My Solution:
# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  start_index = word.find(start)
  end_index = word.find(end)
  if start_index and end_index >=0:
    return word[start_index+1:end_index]
  else:
    return word

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


#QUESTION
# Write a function named count_multi_char_x that takes a string named word and a string
#  named x. This function should do the same thing as the count_char_x function you just 
# wrote - it should return the number of times x appears in word. However, this time, 
# make sure your function works when x is multiple characters long.

# For example, count_multi_char_x("Mississippi", "iss") should return 2
#MY SOLUTION
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):

  return word.count(x)

# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1
#THEIR SOLUTION
def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

  # In our function, we split the first input string using the second input string. 
  # What this does is cut the first string into an array of smaller substrings 
  # containing the parts not equal to our second parameter x. For example, when 
  # splitting "mississippi" with the string "iss", the resulting array will be 
  # [“m”, “”, “ippi”]. This includes the characters before "iss" was found, the 
  # empty space between the two instances of "iss" and the characters after the
  #  last"iss". Be careful! In order to get the correct result we need to return one
  #  less than the total number of split sections — in this example, "iss" was in 
  # the string twice, resulting in 3

###QUESTION###
# Create a function called x_length_words that takes a string named sentence and an 
# integer named x as parameters. This function should return True if every word in 
# sentence has a length greater than or equal to x.
#My SOLUTION
# Write your x_length_words function here:
def x_length_words(sentence, x):
  words_in_sentence = sentence.split()
  for word in words_in_sentence:
    if len(word) >= x:
      return True
    else:
      return False


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

#THEIR SOLUTION
def x_length_words(sentence, x):
  words = sentence.split(" ")
  for word in words:
    if len(word) < x:
      return False
  return True

  #QUESTION
#   Write a function called check_for_name that takes two strings as parameters
#    named sentence and name. The function should return True if name appears
#     in sentence in all lowercase letters, all uppercase letters, or with any 
#     mix of uppercase and lowercase letters. The function should return False
#      otherwise.
#MY SOLUTION
    # Write your check_for_name function here:
def check_for_name(sentence, name):
  name = name.lower()
  sentence = sentence.lower()
  if name in sentence:
    return True
  return False


# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False

#THEIR SOLUTION
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

#QUESTION
# Create a function named every_other_letter that takes a string named word as a parameter. 
# The function should return a string containing every other letter in word.

#MY SOLUTION
# Write your every_other_letter function here:
def every_other_letter(word):
  new_word = ''
  for letter in word[::2]:
    new_word += letter
  return new_word

# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 

#THEIR SOLUTION
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other
#   In order to alternate which character is added to the every_other string, we use a range 
#   of indices which starts at index 0 (the beginning of our word) and ends at the end of our 
#   word. The third parameter in the range function determines what value to increment by. In 
#   this case, we want to increment by 2 in order to get every other letter.

# Another way to loop through all indices of our original string, but only add the letters 
# that correspond to an even index. As a challenge, try solving this problem that way!

#QUESTION
# This one is similar to the last challenge. Instead of selecting every other letter, 
# we want to reverse the entire string. This can be performed in a similar manner, 
# but we will need to modify the range we are using. Here is what we need to do:
# Define the function to accept one parameter for the string
# Create a new empty string to hold the reversed string
# Loop through the input string by starting at the end, and working towards the beginning
# Inside the loop, append the character at the current location to the new string we initialized earlier
# Return the result

#MY SOLUTION
# Write your reverse_string function here:
def reverse_string(word):
  return word[::-1]

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

#THEIR SOLUTION
def reverse_string(word):
  reverse = ""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

# This is similar to the last solution, but our range has been modified in order to start at the last index 
# of the string (length of the string minus one) up to the first index. Since the parameter for the ending index
#  is exclusive we need to provide the index of one more iteration than what we want to stop at. We want to stop 
#  at 0, and since we are incrementing by -1, we will set the ending index to -1. Finally, make sure to add the 
#  third parameter of -1. This makes us increment by -1 at each step.

#QUESTION
# Write a function called make_spoonerism that takes two strings as parameters named word1 and word2. Finding 
# the first syllable of a word is a difficult task, so for our function, we’re going to switch the first letters 
# of each word. Return the two new words as a single string separated by a space.
#MY SOLUTION
# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
  new_word1 = word2[0] + word1[1:]
  new_word2 = word1[0] + word2[1:]
  return new_word1 + " " + new_word2

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a

#THEIR SOLUTION
def make_spoonerism(word1, word2):
  return word2[0]+word1[1:]+" "+word1[0]+word2[1:]

#QUESTION
# Create a function named add_exclamation that has one parameter named word. This function should add 
# exclamation points to the end of word until word is 20 characters long. If word is already at least 20 
# characters long, just return word.

#MY SOLUTION

# Write your add_exclamation function here:
def add_exclamation(word):
  if len(word) >= 20:
    return word
  else:
    exclamations = 20 - len(word)
    return word + "!" * exclamations

# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn

#THEIR SOLUTION
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word

# This function shows how we can continuously append to our string based on some condition. In this case,
#  we keep testing the length of the string to see if we should keep going. Once the length has reached 20, 
#  either by adding exclamation marks or by already being long, we return the result.