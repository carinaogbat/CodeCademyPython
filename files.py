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



#=> ['Name,Age,ID\n', 
# 'Richard Andrews,43,0de2ecf31df2386377b1d2dc4fae8b16fad05ad0 
# \n', 'Hailey Sellers,24,3d9b8a95458c1df2687191e8146a97ca4afb28aa          
# \n', 'Jessica Pace,39,a5daa63ef893cb86bc8df1110cc9a5f8e1d0c563            
# \n', 'Jasmine Escobar,42,9844e403841ec84b9a2fb3caf9d2a1c9ee042d31         
# \n', 'Karen Kelly,26,8338f76ac0e9a76d73d57790f1d9843b185b5428             
# \n', 'Patricia Christensen,70,23099bb630c1c64989458393045f08de3bac0eb9    
# \n', 'Jessica Hansen,24,a8c035ccd099ef909a46e0d96b76c0f132c9c562          
# \n', 'Raymond Adams,53,a051901830ff6c2095524ef92b1541eef9f8c64d           
# \n', 'Stephanie Morrow,53,3bad04a5fc0a7ec33735ae45535f354887988f35        
# \n', 'Timothy Ramos,34,b4930920b5256c4e592541297e43a556c8fe33a8 \n', '\n']

#Python has another option for reading csv files, convertin the data into a dictionary using the csv library’s 
# DictReader object. Here’s how we’d create a list of the email addresses of all of the users in the above table:
import csv
 
list_of_email_addresses = []
with open('users.csv', newline='') as users_csv: #We pass the additional keyword argument newline='' to the file opening 
                                                #open() function so that we don’t accidentally mistake a line break in 
                                                # one of our data fields as a new row in our CSV 
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])


