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

