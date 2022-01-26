class HashSet:

  def __init__(self, max_size=10) :
      
      self.arr =  [None] * max_size
  
  def add(self, item):
    index = hash(item) % len(self.arr)
    if self.arr[index] == None or self.arr[index] == item:
      self.arr[index] = item
    else:
      i = 1
      done = False
      while not done:
        new_index = (index + i) % len(self.arr)

        if new_index == index:
          raise ValueError("Hash table is full!")
        if new_index == len(self.arr)-1:
            raise ValueError("Item not in table")
        else:
          if self.arr[new_index] is None or self.arr[new_index] == item:
            self.arr[new_index] = item
            done = True
            return new_index          
          else:
            i += 1
       
        
  def index_of(self, item):

    index = hash(item)%len(self.arr)
    initialIndex = index
    while self.arr[index] != item and (index+1)%len(self.arr) != initialIndex and self.arr[(index+1)%len(self.arr)] is not None:
      print(index)
      index = (index+1)%len(self.arr)
    if self.arr[index] == item:
      return index
    print(index)
    return -1

    # index = hash(item) % len(self.arr)
    # if self.arr[index] == item:
    #   return index
    # else:
    #   i = 1
    #   done = False
    #   while not done:
    #     new_index = (index + i) % len(self.arr)
    #     if self.arr[new_index] == item:
    #       done = True
    #       return new_index
          
    #     else: 
    #       if i == len(self.arr) -1:
    #         return -1
    #       else:
    #         i += 1

  def delete(self, item):
      index = hash(item) % len(self.arr)
      if self.arr[index] == item:
        self.arr[index] = False
        return True
      else:
        i = 1
        done = False
        while not done:
          new_index = (index + i) % len(self.arr)
          if self.arr[new_index] == item:
            self.arr[index] = None
            done = True
          else:
            if new_index == len(self.arr) -1:
              return False
            else:
              i += 1