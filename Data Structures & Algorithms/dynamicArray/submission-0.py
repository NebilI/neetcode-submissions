class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * capacity


    def get(self, i: int) -> int:
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        self.size = max(i,self.size)


    def pushback(self, n: int) -> None:
        if self.size < self.capacity:
            self.set(self.size,n)
        else:
            self.resize()
            self.set(self.size , n)
        self.size +=1

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size]
 
    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(0,len(self.arr)):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity