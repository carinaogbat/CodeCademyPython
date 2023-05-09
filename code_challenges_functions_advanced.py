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