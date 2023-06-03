#importing our node class (must be a doubly linked node class because
# queues have heads and tails)
class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value

class Queue:
  # Add max_size and size properties within __init__():
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0

      # Add your enqueue method below:
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print('Adding ' + str(item_to_add.get_value()) + ' to the queue!')
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
    
  def peek(self):
    if self.is_empty():
      print("Nothing to see here")
    else:
      return self.head.get_value()
  
  # Define get_size() and has_space() below:
  def get_size(self):
    return self.size

  def has_space(self):
    if self.max_size == None:
      return True
    elif self.max_size > self.get_size():
      return True
    else:
      return False

  def is_empty(self):
    if self.size > 0:
      return False
    else:
      return True
