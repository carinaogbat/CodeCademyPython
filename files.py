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
