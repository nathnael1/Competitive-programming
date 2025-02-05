class RandomizedSet:

    def __init__(self):
        #intializing set
        self.set1 = set()

    def insert(self, val: int) -> bool:
        if val in self.set1:
            return False
        self.set1.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.set1:
            self.set1.discard(val)
            return True
        return False
    def getRandom(self) -> int:
        return random.choice(list(self.set1))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()