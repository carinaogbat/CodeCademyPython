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
for drink in zipped_drinks:
  #prints ('espresso', 64)
  # ('chai', 40)
  # ('decaf', 0)
  # ('drip', 120)
drinks_to_caffeine = {key:value for key, value in zip(drinks, caffeine)}
print(drinks_to_caffeine)
  #prints {'espresso': 64, 'chai': 40, 'decaf': 0, 'drip': 120}