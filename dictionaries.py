###Add a Key ###
animals_in_zoo = {}
animals_in_zoo['zebras'] = 8
animals_in_zoo['monkeys'] = 12
animals_in_zoo['dinosaurs'] = 0

###ADD Multiple Keys###
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({'theLooper': 138475, 'stringQueen': 85739})
print(user_ids)
  # prints 
# {'teraCoder': 9018293, 'proProgrammer': 119238, 'theLooper': 138475, 'stringQueen': 85739}

###Overwrite Values###
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

###DICTIONARY COMPREHENSIONS***
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
#zip() combines two lists into an iterator of tuples with the list elements paired together
zipped_drinks = zip(drinks, caffeine)
for drink in zipped_drinks:
  print(drink)
  #prints ('espresso', 64)
  # ('chai', 40)
  # ('decaf', 0)
  # ('drip', 120)
  ## Using dictionary comprehension to zip into a dictionary
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
print(drinks_to_caffeine)
  #prints {'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}

#GET A KEY
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
#.get allows you to check for a key and put a default value if the key is not present, by defauly it will return None
tc_id = user_ids.get("teraCoder", 'No value')
print(tc_id)
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)

#DELETE A KEY WITH .POP()
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
#you are adding stamina grains to health points and simultaneously removing stamina grains from the dictionary, if the key does not exist you are putting a default value of 0
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)
print(available_items)
print(health_points)

##GET ALL KEYS33
#can use list() function to get a list of all keys (ie list(user_ids))
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
print(list(user_ids))
#=> ['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith']
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
#can use .keys() method to return a dictionary keys object, the object returned is a set of keys in the dictionary, you can't add or remove elements from the boject but it can be used in place of a list for iteration
users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
#=> dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])
print(lessons)
#=> dict_keys(['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries'])

###GET ALL VALUES 333
#no built in function to get all values as a list but you can use list(dictionary.values())
#Dictionaries have a .values() method that returns a dict_values object (like a dict_keys object but for values) with all of the values in the dictionary. It can be used in the place of a list for iteration:
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for exercise in num_exercises.values():
  total_exercises += exercise
print(total_exercises)

###GET ALL ITEMS (KEYS AND VALUES)
#can get both the keys and values with the .items() method, it returns a dict_list object with each element consistenting of a tuple of (key, value)
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for position, title in pct_women_in_occupation.items():
  print(f'Women make up {title} percent of {position}s')

