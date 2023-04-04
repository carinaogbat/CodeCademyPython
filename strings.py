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

