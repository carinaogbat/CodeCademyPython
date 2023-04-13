#using open to read a file amd readlines() to read each line in file
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)
#=> 1. How many lines do we write on the daily,
#2. Many money, we write many many many
#3. How many lines do you write on the daily,
#4. Say you say many money, you write many many many#=>

#if you don't want to read all files there is a .readline() method
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)

#can create a new file with open function and "w" (write) argument,
#default argument for open is "r" (to read)
with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write("One Direction")

#you can also use open to add to a file with the "a" argument
with open("cool_dogs.txt", "a") as cool_dogs_file:
  cool_dogs_file.write("\nAir Buddy") #this will add Air Buddy to the file as a newline

##using with open() vs open()
#it's better to open a file using the with block because everything indented inside the block will run and then close 
# the file when the block is closed. If you open just with open() the file will not close until you write close(). 
# This can impact performance as files exist outside of your Python script and other programs on your computer 
# may be trying to access the file.

fun_cities_file = open('fun_cities.txt', 'a')
 
# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")
 
# But we need to remember to close the file
fun_cities_file.close()

with open('fun_file.txt') as close_this_file:

  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)

#CSV files are a text file that impose a structure to their data, CSV stands for comma separated value and they 
# are usually the way that data from spreadsheet software (such as microsoft xl or google sheets) in exported 
# in a poratable format. The first row of a CSV will usally represent the labels of the data rather than the data.
with open('logger.csv') as log_csv_file:
  line = log_csv_file.readlines()
  print(line)


