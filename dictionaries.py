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