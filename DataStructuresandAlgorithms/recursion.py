#BUILDING A STACK TO DEMONSTRATE RECURSION
# define your sum_to_one() function above the function call
def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")

  while len(call_stack) != 0:
    return_value = call_stack[-1]
    call_stack.remove(return_value)
    print(call_stack)
    print(f"Adding return value {return_value['n_value']} to result {result}")
    result += return_value['n_value']
  return result, call_stack

sum_to_one(4)

#SUM TO ONE WITH RECURSION
#O(N) - LINEAR
# Define sum_to_one() below...
def sum_to_one(n):
  if n == 1:
    return n
  print(f'Recursing with input {n}')
  return n + sum_to_one(n-1)

# uncomment when you're ready to test
print(sum_to_one(7))

#POWER SET
def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first
  
universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)

#PRINTS ['MIT', 'UCLA', 'Stanford', 'NYU']
# ['MIT', 'UCLA', 'Stanford']
# ['MIT', 'UCLA', 'NYU']
# ['MIT', 'UCLA']
# ['MIT', 'Stanford', 'NYU']
# ['MIT', 'Stanford']
# ['MIT', 'NYU']
# ['MIT']
# ['UCLA', 'Stanford', 'NYU']
# ['UCLA', 'Stanford']
# ['UCLA', 'NYU']
# ['UCLA']
# ['Stanford', 'NYU']
# ['Stanford']
# ['NYU']
# []

#FLATTEN A LIST
# define flatten() below...
def flatten(my_list):
  result = []
  for item in my_list:
    if isinstance(item, list):
      print("list found!")
      flat_list = flatten(item)
      result += flat_list
    else:
      result.append(item)

  return result


### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]

print(flatten(planets))
#PRINTS ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']

#FIBONACCIS
# define the fibonacci() function below...
def fibonacci(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  print(f'value of n is currently: {n}')

  return fibonacci(n-2) + fibonacci(n-1)

fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"
#PRINTS 1234567891011121314
# define the fibonacci() function below...
def fibonacci(n):
  if n == 1:
    return 1
  if n == 0:
    return 0
  print(f'value of n is currently: {n}')

  return fibonacci(n-2) + fibonacci(n-1)

fibonacci(5)
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
fibonacci_runtime = "2^N"
#PRINTS
# value of n is currently: 5
# value of n is currently: 3
# value of n is currently: 2
# value of n is currently: 4
# value of n is currently: 2
# value of n is currently: 3
# value of n is currently: 2

#BUILD BINARY SEARCH TREE WITH DICTIONARY
# Define build_bst() below...
def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"
  middle_idx = len(my_list) // 2
  #if you just use one / you will get a floating number, that's why you have to use //
  middle_value = my_list[middle_idx]
  print(f'Middle index: {middle_idx}')
  print(f'Middle value: {middle_value}')
  tree_node = {'data': middle_value}
  tree_node['left_child'] = build_bst(my_list[: middle_idx])
  tree_node['right_child'] = build_bst(my_list[middle_idx + 1:])
  return tree_node


# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"
# N is the length of our input list.

# Our tree will be logN levels deep, meaning there will logN times where a new parent-child relationship is created.

# If we have an 8 element list, the tree is 3 levels deep: 2**3 == 8.

# Each recursive call is going to copy approximately N elements when the left and right halves of the list are passed to the recursive calls. We’re reducing by 1 each time (the middle_value), but that’s a constant factor.

# Putting that together, we have N elements being copied logN levels for a big O of N*logN.
