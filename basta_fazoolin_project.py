class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return f"Franchise Address: {self.address}"

  def available_menus(self, time):
    available_menus_list = []
    for menu in self.menus:
      if time in range(menu.start_time, menu.end_time+1):
        available_menus_list.append(menu)
    return available_menus_list


class Menu:

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f"Menu: {self.name}, available from: {self.start_time}-{self.end_time}"

  def calculate_bill(self, purchased_items):
    total_bill = 0
    for item in purchased_items:
      if item in self.items:
        total_bill += self.items[item]
    return total_bill



brunch = Menu("brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 1100, 1600
 )

early_bird = Menu("early bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, 1500, 1800)

dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, 1700, 2300)

kids = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 1100, 2100)

# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
print(flagship_store)
print(new_installment)
print(flagship_store.available_menus(2100))

#Arepa
arepas_menu = Menu("Take a' Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 1000, 2000)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepa = Business("Take a' Arepa", [arepas_place])
print(arepa.franchises[0])



