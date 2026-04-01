class MyHashSet:
    
    def __init__(self):
        # Decide Data Structure
        self.DS = dict()

    def add(self, key: int) -> None:
        # O(log(n)) operation
        self.DS[key] = True

    def remove(self, key: int) -> None:
        # O(log(n)) operation
        self.DS[key] = False

    def contains(self, key: int) -> bool:
        # O(1) operation
        if (key in self.DS.keys()):
            return self.DS[key]
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)