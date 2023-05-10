# Write a function named first_three_multiples() that has one parameter named num.

# This function should print the first three multiples of num. Then, it should return the
#  third multiple.

# For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines,
#  and return 21.

#MY SOLUTION (SAME AS THEIRS)
# Write your first_three_multiples function here
def first_three_multiples(num):
  print(num*1)
  print(num*2)
  print(num*3)
  return num* 3

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

#QUESTION
# Create a function called tip() that has two parameters named total and percentage.

# This function should return the amount you should tip given a total and the percentage
#  you want to tip.

# Write your tip function here:
def tip(total, percentage):

  return total * (percentage / 100)

  
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

#QUESTION

# Write a function named introduction() that has two parameters named first_name and last_name.

# The function should return the last_name, followed by a comma, a space, first_name another space,
#  and finally last_name.

#MY ANSWER (THEIRS WAS CONCATONATION)
# Write your introduction function here:
def introduction(first_name, last_name):
  return f'{last_name}, {first_name} {last_name}'

# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou