class List:
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.data = []

    def __getitem__(self, i):      #2 this function is checking if the i is a valid index and returns the index if it is valid or index error if not valid
        if 0 <= i < len(self.data): 
            return self.data[i]
        else:
            raise IndexError("Index error or indeex out of range")

    def __setitem__(self, i, element):   #3 this is basically a setter(meaning it stores the element at the index we found above)
        if 0 <= i < len(self.data):
            self.data[i] = element
        else:
            raise IndexError("insex out of range")

    def __len__(self):               #4 just the number items/elements stored
        return len(self.data)

    def append(self, element):     #5
        self.data.append(element)

    def insert(self, index, element):       #6
        if 0 <= index <= len(self.data):
            self.data.insert(index, element)
        else:
            raise IndexError("Index out of range")

    def __iter__(self):    #7
        return iter(self.data)

    def pop(self, i=None):         #8 
        if i is None:
            if len(self.data) > 0:
                return self.data.pop()
            else:
                raise IndexError("Popping from empty list not possible")
        elif 0 <= i < len(self.data):
            return self.data.pop(i)
        else:
            raise IndexError("Index out of range")

    def remove(self, target):                   #9
        if target in self.data:
            self.data.remove(target)
        else:
            raise ValueError("Element is not in list")

    def __contains__(self, element):                  #10
        return element in self.data
