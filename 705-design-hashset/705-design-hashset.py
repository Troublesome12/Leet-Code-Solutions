class MyHashSet:

    def __init__(self):
        self.myArray = []

    def add(self, key: int) -> None:
        self.myArray.append(key)

    def remove(self, key: int) -> None:
        for val in self.myArray:
            if val == key:
                self.myArray.remove(val)
                self.remove(key)
                break

    def contains(self, key: int) -> bool:
        if key in self.myArray:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)