class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [None for size in range(self.array_size)]
  
  def hash(self, key):
    return sum(key.encode())

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(key.hash())
    self.array[array_index] = [key, value]