#STRING INDEXING
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


#string immutability (need to create new string to change string)
first_name = "Bob"
last_name = "Daily"
fixed_first_name = "R" + first_name[-2:]
##get R plus ob to have "Rob"

#escape characters
password = "theycallme\"crazy\"91"
##add backslash escape at beginning of ' and before end of '

#iterating through strings
def get_length(string):
  count = 0
  for char in string:
    count += 1
  return count

#string conditionals
def contains(big_string, little_string):
  return little_string in big_string

# def common_letters(string_one, string_two):
#   common_letters = []
#   for char in string_one:
#     if char in string_one and char in string_two:
#       if char not in common_letters:
#         common_letters.append(char)
#   return common_letters

#better way to solve:
def common_letters(string_one, string_two):
  common_letters = []
  for char in string_one:
    if char in string_two and char not in common_letters:
      common_letters.append(char)
  return common_letters

print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False
print("e" in "blueberry")
# => True
print("a" in "blueberry")
# => False

#using range and length to shift by index
# the function should generate the username AbeSimp from Abe Simpson
def username_generator(first_name, last_name):
  return first_name[:3] + last_name[:4]

#this function should shift all letters of username to the right. "apple" becomes "epple"
def password_generator(user_name):
  password = ""
  for i in range(0, len(user_name)):
    password += user_name[i-1]
  return password

#STRING METHODS:
# str.lower() - all lowercase
# str.upper() - all uppercase
# str.title() - capitalizes all first letters
# str.split() - splits at spaces as default, otherwise by delimeter var.split('delimeter')
# delimeter.join(str) - ' '.join(str) - joins at delimeter delimeter.join(str)
# str.strip() - removes all whitespace characters from beginning to end, you can also strip
    #with a character argument str.strip('!') *note this will only strip argument and not spaces
# str.replace(' ', '.') - takes two arguments and replaces all instances of first argument with second argument
# str.find('t') - takes string as argument and returns first index value where string is located
# str.format(var, var) - takes variables as an argument and includes them in string it is run on by
    #using {} as placeholders
    #*** note you can now use keywords so you don't have to focus on placement
test_title = 'the cat in the hat'
test_title = test_title.title()
print(test_title) # prints The Cat In The Hat

#get last names through a for loop, string splitting, and indexing
authors = """Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,
Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"""
author_names = authors.split(',')
author_last_names = []
for author in author_names:
  author_last_names.append(author.split()[-1])
print(author_last_names)
#prints 12345768
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(',')
author_last_names = []
for author in author_names:
  author_last_names.append(author.split()[-1])
print(author_last_names)
#prints ['Lorde', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']

#can split strings with escape characters
#.split('\n') - splits by line breaks
#.split('\t') - splits by tabs
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
..."""

spring_storm_lines = spring_storm_text.split('\n')
print(spring_storm_lines)
# prints ['The sky has given over ', 'its bitterness. ', 'Out of the dark change ', 'all day long ', 
# 'rain falls and falls ', 'as if it would never end. ']

#REMEMBER TO JOIN STRINGS YOU START WITH DELIMETER FIRST " ".JOIN(MY_VAR), TO SPLIT YOU START WITH VAR
# FIRST MY_VAR.SPLIT(' ') 
#JOINING STRINGS 'delimiter'.join(list_you_want_to_join)
# my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
# print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_words)

santana_songs = ['Oye Como Va', 'Smooth', 'Black Magic Woman', 'Samba Pa Ti', 'Maria Maria']
santana_songs_csv = ','.join(santana_songs)
print(santana_songs_csv)
# => 'Oye Como Va,Smooth,Black Magic Woman,Samba Pa Ti,Maria Maria'
#can also join using escape characters 
smooth_fifth_verse_lines = ['Well I\'m from the barrio', 'You hear my rhythm on your radio']
smooth_fifth_verse = '\n'.join(smooth_fifth_verse_lines)
print(smooth_fifth_verse)
#Well I'm from the barrio
#You hear my rhythm on your radio

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
love_maybe_lines_stripped = []
for string in love_maybe_lines: #can't use strip on a list so you have to run a for loop
  love_maybe_lines_stripped.append(string.strip())
print(love_maybe_lines_stripped)
#prints ['Always', 'in the middle of our bloodiest battles', 'you lay down your arms', 'like flowering mines', '', 'to conquer me home.']
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)
#=> Always
# in the middle of our bloodiest battles
# you lay down your arms
# like flowering mines

# to conquer me home.

god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement) 
#=> 20

def poem_title_card(title, poet):
  return 'The poem "{}" is written by {}.'.format(title, poet)
print(poem_title_card("Endless Love", "Mauschen"))
# => The poem "Endless Love" is written by Mauschen.

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)
highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
print(highlighted_poems_stripped)
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))
titles = []
poets = []
dates = []
for item in highlighted_poems_details:
  titles.append(item[0])
  poets.append(item[1])
  dates.append(item[2])
for i in range(0,len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(titles[i], poets[i], dates[i]))

# => The poem Afterimages was published by Audre Lorde in 1997
# The poem The Shadow was published by William Carlos Williams in 1915
# The poem Ecstasy was published by Gabriela Mistral in 1925
# The poem Georgia Dusk was published by Jean Toomer in 1923
# The poem Parting Before Daybreak was published by An Qi in 2014
# The poem The Untold Want was published by Walt Whitman in 1871
# The poem Mr. Grumpledump's Song was published by Shel Silverstein in 2004
# The poem Angel Sound Mexico City was published by Carmen Boullosa in 2013
# The poem In Love was published by Kamala Suraiyya in 1965
# The poem Dream Variations was published by Langston Hughes in 1994
# The poem Dreamwood was published by Adrienne Rich in 1987

