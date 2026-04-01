import queue
class MyStack:
    
    def __init__(self):
        self.Q1 = queue.Queue()
        self.Q2 = queue.Queue()
        self.EnableQ = True

    def push(self, x: int) -> None:
        if (self.EnableQ):
            self.Q1.put(x)
        else:
            self.Q2.put(x)

    def pop(self) -> int:

        if (self.EnableQ):
            while not self.Q1.empty():
                item = self.Q1.get()
                if(self.Q1.empty()):
                    self.EnableQ = False
                    return item
                self.Q2.put(item)
        else:
            while not self.Q2.empty():
                item = self.Q2.get()
                if(self.Q2.empty()):
                    self.EnableQ = True
                    return item
                self.Q1.put(item)

    def top(self) -> int:
        if (self.EnableQ):
            while not self.Q1.empty():
                item = self.Q1.get()
                self.Q2.put(item)
                if(self.Q1.empty()):
                    self.EnableQ = False
                    return item
                
        else:
            while not self.Q2.empty():
                item = self.Q2.get()
                self.Q1.put(item)
                if(self.Q2.empty()):
                    self.EnableQ = True
                    return item
                

    def empty(self) -> bool:
        
        if (self.EnableQ):
            return self.Q1.empty()
        else:
            return self.Q2.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()