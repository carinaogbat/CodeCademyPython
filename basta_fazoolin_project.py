class Menu:

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f"Menu: {self.name}, available from: {self.start_time}-{self.end_time}"

    # def calculate_bill(self, purchased_items):
    #   total_bill = 0
    #   for item in purchased_items:
    #     if item in self.items:
    #       total_bill +=  




brunch = Menu(name="brunch", items={
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, start_time=1100, end_time=1600
 )

early_bird = Menu(name="early bird", items={'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, start_time=1500, end_time=1800)

dinner = Menu(name="dinner", items= {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, start_time=1700, end_time=2300)

kids = Menu(name="kids", items={'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, start_time=1100, end_time=2100)

print(brunch)