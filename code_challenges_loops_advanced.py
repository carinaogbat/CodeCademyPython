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
#***QUESTION***
# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
# The function should sum the elements of the list until the sum is greater than 9000. When this happens, 
# the function should return the sum. If the sum of all of the elements is never greater than 9000, the function
# should return total sum of all the elements. If the list is empty, the function should return 0.
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

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


#****QUESTION****
# Create a function named max_num() that takes a list of numbers named nums as a parameter.

# The function should return the largest number in nums
#MY SOLUTION
#Write your function here
def max_num(nums):
  max_num = nums[0]
  for num in nums:
    if num > max_num:
      max_num = num
  return max_num


#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

#THEIR SOLUTION
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum