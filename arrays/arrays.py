import sys
import ctypes

n = 10
data= []

for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; size in bytes: {1:4d} '.format(a, b))
    data.append(n)

#dynamic arrays
class DynamicArray(object):
    
    def __init__(self):

        self.n = 0
        self.capacity = 1
        self.array = self.makeArray(self.capacity)

    def __len__(self):

        return self.n
    
    def __getitem__(self, k):

        if not 0 <= k < self.n:
            return IndexError('{} is out of bounds'.format(k))
        return self.array[k]

    def append(self, element):
        
        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.array[self.n] = element
        self.n += 1

    def _resize(self, newCap):
        
        newArray = self.makeArray(newCap)
        for k in range(self.n):
            newArray[k] = self.array[k]
        self.array = newArray
        self.capacity = newCap

    def makeArray(self, newCap):
        
        return (newCap * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(3)
print('Length: ', len(arr))
for i in range(len(arr)):
    print(arr[i])

