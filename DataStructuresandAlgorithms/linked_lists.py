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

  def insert_end(self, new_value):
    new_node = Node(new_value)
    current_node = self.get_head_node()
    next_node = current_node.get_next_node()
    while current_node:
      if current_node.get_next_node() == None:
        current_node.set_next_node(new_node)
        current_node = None
      else:
        current_node = next_node
    

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

#TWO POINTER LINKED LIST TECHNIQUES
#TWO POINTERS MOVING IN PARALLEL
def nth_last_node(linked_list, n):
  current = None
  tail_seeker = linked_list.head_node
  count = 1
  while tail_seeker:
    tail_seeker = tail_seeker.get_next_node()
    count += 1
    if count >= n + 1:
      if current is None:
        current = linked_list.head_node
      else:
        current = current.get_next_node()
  return current
       

#POINTERS AT DIFFERENT SPEEDS
#POINTER ONE TWICE AS FAST AS POINTER TWO
# from LinkedList import LinkedList

# Complete this function:
def find_middle(linked_list):
  fast_pointer = linked_list.head_node
  slow_pointer = linked_list.head_node
  while fast_pointer is not None:
    fast_pointer = fast_pointer.get_next_node()
    if fast_pointer is not None:
      fast_pointer = fast_pointer.get_next_node()
      slow_pointer = slow_pointer.get_next_node()
  return slow_pointer

def generate_test_linked_list(length):
  linked_list = LinkedList()
  for i in range(length, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your code:
test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)
#added handwritten linked list notes

###DOUBLY LINKED LIST
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
    

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None

  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)
    self.head_node = new_head
    # current_tail = self.tail_node
    if self.tail_node is None:
      self.tail_node = new_head

 def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)

    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail

  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None

    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()

    return removed_head.get_value()

