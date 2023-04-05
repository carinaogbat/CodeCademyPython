#STRING INDEXING
first_name = "Reiko"
last_name = "Matsuki"
def password_generator(first_name, last_name):
  return first_name[-3:] + last_name[-3:]

temp_password = password_generator(first_name, last_name)
print(temp_password) ##logs ikouki

#negative indices
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(second_to_last) #prints f
print(final_word) #prints life


#string immutability (need to create new string to change string)
first_name = "Bob"
last_name = "Daily"
fixed_first_name = "R" + first_name[-2:]
##get R plus ob to have "Rob"

#escape characters
password = "theycallme\"crazy\"91"
##add backslash escape at beginning of ' and before end of '

#iterating through strings
def get_length(string):
  count = 0
  for char in string:
    count += 1
  return count

#string conditionals
def contains(big_string, little_string):
  return little_string in big_string

# def common_letters(string_one, string_two):
#   common_letters = []
#   for char in string_one:
#     if char in string_one and char in string_two:
#       if char not in common_letters:
#         common_letters.append(char)
#   return common_letters

#better way to solve:
def common_letters(string_one, string_two):
  common_letters = []
  for char in string_one:
    if char in string_two and char not in common_letters:
      common_letters.append(char)
  return common_letters

print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False
print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False

#using range and length to shift by index
# the function should generate the username AbeSimp from Abe Simpson
def username_generator(first_name, last_name):
  return first_name[:3] + last_name[:4]

#this function should shift all letters of username to the right. "apple" becomes "epple"
def password_generator(user_name):
  password = ""
  for i in range(0, len(user_name)):
    password += user_name[i-1]
  return password

#STRING METHODS:
# .lower() - all lowercase
# .upper() - all uppercase
# .title() - capitalizes all first letters
# .split() - splits at spaces as default, otherwise by delimeter .split('delimeter')
test_title = 'the cat in the hat'
test_title = test_title.title()
print(test_title) # prints The Cat In The Hat

#get last names through a for loop, string splitting, and indexing
authors = """Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,
Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"""
author_names = authors.split(',')
author_last_names = []
for author in author_names:
  author_last_names.append(author.split()[-1])
print(author_last_names)
#prints 12345768
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(',')
author_last_names = []
for author in author_names:
  author_last_names.append(author.split()[-1])
print(author_last_names)
#prints ['Lorde', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']

  

#can split strings with escape characters
#.split('\n') - splits by line breaks
#.split('\t') - splits by tabs
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
..."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)
# prints ['The sky has given over ', 'its bitterness. ', 'Out of the dark change ', 'all day long ', 
# 'rain falls and falls ', 'as if it would never end. ']

#JOINING STRINGS 'delimiter'.join(list_you_want_to_join)
# my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
# print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_words)