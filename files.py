#using open to read a file amd readlines() to read each line in file 
# ***can also just use read() to get entire thing as string
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

#Python has another option for reading csv files, converting the data into a dictionary using the csv library’s 
# DictReader object. Here’s how we’d create a list of the email addresses of all of the users in the above table:
import csv
 
list_of_email_addresses = []
with open('users.csv', newline='') as users_csv: #We pass the additional keyword argument newline='' to the file opening 
                                                #open() function so that we don’t accidentally mistake a line break in 
                                                # one of our data fields as a new row in our CSV 
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])

import csv
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row["Cool Fact"])

#csv files are not just separated by commas, they can have different delimeters besides commas, you just have to specify the delimiter in the DictReader call
import csv
with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter="@")
  isbn_list = []
  for row in books_reader:
    isbn_list.append(row["ISBN"])

#you can also write csv files: We import the csv library, and then open a new CSV file in write-mode by passing the 'w' argument to the open() function.

# We then define the fields we’re going to be using into a variable called fields. We then instantiate our CSV writer object and pass two arguments. The first is output_csv, the file handler object. The second is our list of fields fields which we pass to the keyword parameter fieldnames.

# Now that we’ve instantiated our CSV file writer, we can start adding lines to the file itself! First we want the headers, so we call .writeheader() on the writer object. This writes all the fields passed to fieldnames as the first row in our file. Then we iterate through our big_list of data. Each item in big_list is a dictionary with each field in fields as the keys. We call output_writer.writerow() with the item dictionaries which writes each line to the CSV file.

access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
with open("logger.csv", "w") as logger_csv:
  # fields = ["time", "limit", "address"] I wrote fields but didn't have to because it was already in code above
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

  log_writer.writeheader()
  for item in access_log:
    log_writer.writerow(item)

#can also import json and use open and json.load() to open and parse json files into a Python dictionary
import json
with open("message.json") as message_json:
  message = json.load(message_json)
  print(message['text'])


#you can also parse a python dictionary and turn it into a json file using open and the json.dump() method
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

import json

with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)




