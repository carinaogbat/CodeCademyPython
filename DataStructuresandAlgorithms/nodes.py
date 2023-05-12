#creating a Node Class

# Create the Node class below:
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

#We need methods to access the data and link within the node. For this, we will use two getters, .get_value() and .get_link_node().
# These should each return their corresponding value on the self object.   

  # Define your get_value and get_link_node methods below:
  def get_value(self):
    return self.value
  
  def get_link_node(self):
    return self.link_node

#We are only allowing the value of the node to be set upon creation. However, we want to allow updating the link of the node. For this, we will use a setter to modify the self.link_node attribute.
# The method should be called .set_link_node() and should take link_node as an argument. It should then update the self.link_node attribute as appropriate.
  
  # Define your set_link_node method below:
  def set_link_node(self, link_node):
    self.link_node = link_node

# Add your code below:
#CREATING AND TRAVELING NODES
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

yacko.set_link_node(dot)
dot.set_link_node(wacko)

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()
print(dots_data) # => enjoys spending time in movie lots
print(wackos_data) #=> has a penchant for hoarding snacks
print(yacko.get_value()) #=> likes to yak
get_to_wacko = yacko.get_link_node().get_link_node().get_value()
print(get_to_wacko) #=> has a penchant for hoarding snacks
