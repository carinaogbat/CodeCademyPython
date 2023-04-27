# Create a function named larger_sum() that takes two lists of numbers as parameters 
# named lst1 and lst2.

# The function should return the list whose elements sum to the greater number. 
# If the sum of the elements of each list are equal, return lst1.

#Write your function here ***MY SOLUTION***
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for num in lst1:
    sum1 += num
  for num in lst2:
    sum2 += num
  
  if sum1 == sum2:
    return lst1
  elif sum1 > sum2:
    return lst1
  else:
    return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

# ***THEIR SOLUTION ***
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2

#MY SOLUTION
#Write your function here
def over_nine_thousand(lst):
  if len(lst) == 0:
    return 0
  else:
    sum = 0
    for num in lst:
      sum += num
      if sum > 9000:
        return sum
    return sum



#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#THEIR SOLUTION
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum