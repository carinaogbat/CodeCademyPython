#first create a Node that can set values, get next node, and set next node
# Define your Node class below:
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
  
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

my_node = Node(44)
print(my_node.get_value()) #=> 44

#With the Node in hand, we can start building the actual linked list. Depending on the end-use 
# of the linked list, a variety of methods can be defined.
# For our use, we want to be able to:
# get the head node of the list (it’s like peeking at the first item in line)
# add a new node to the beginning of the list
# print out the list values in order
# remove a node that has a particular value
# Let’s get started!

# Create your LinkedList class below:
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node

#Next up, we’ll define methods for our LinkedList class that allow us to:
# insert a new head node
# return all the nodes in the list as a string so we can print them out in the terminal!

# We'll be using our Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
# Add your insert_beginning and stringify_list methods below:
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node

  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) +"\n"
      current_node = current_node.get_next_node()
    return string_list

# Test your code by uncommenting the statements below - did your list print to the terminal?
# ll = LinkedList(5)
# ll.insert_beginning(70)
# ll.insert_beginning(5675)
# ll.insert_beginning(90)
# print(ll.stringify_list())
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
        self.head_node = current_node.get_next_node()
    else:
        while current_node:
            next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
            current_node.set_next_node(next_node.get_next_node())
            current_node = None
        else:
            current_node = next_node
       