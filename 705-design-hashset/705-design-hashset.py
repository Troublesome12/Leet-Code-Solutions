class MyHashSet:

    def __init__(self):
        self.myDict = {}

    def add(self, key: int) -> None:
        if key in self.myDict.keys():
            self.myDict[key] += 1
        else:
            self.myDict[key] = 1

    def remove(self, key: int) -> None:
        if key in self.myDict.keys():
            del self.myDict[key]

    def contains(self, key: int) -> bool:
        if key in self.myDict.keys():
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)