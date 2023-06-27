# Hash map: A key-value store that uses an array and a hashing function to save and retrieve values.
# Key: The identifier given to a value for later retrieval.
# Hash function: A function that takes some input and returns a number.
# Compression function: A function that transforms its inputs into some smaller range of possible outputs.

# Recipe for saving to a hash table:
# - Take the key and plug it into the hash function, getting the hash code.
# - Modulo that hash code by the length of the underlying array, getting an array index.
# - Check if the array at that index is empty, if so, save the value (and the key) there.
# - If the array is full at that index continue to the next possible position depending on your collision strategy.

# Recipe for retrieving from a hash table:
# - Take the key and plug it into the hash function, getting the hash code.
# - Modulo that hash code by the length of the underlying array, getting an array index.
# - Check if the array at that index has contents, if so, check the key saved there.
# - If the key matches the one you're looking for, return the value.
# - If the keys don't match, continue to the next position depending on your collision strategy.


class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    self.array[array_index] = value

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    return self.array[array_index]