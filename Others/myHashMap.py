"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
"""

# time complexity: O(n), every operation would need to traverse the array
# space complexity: O(n), expands as every put operation
class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        for tup in self.arr:
            if key == tup[0]:
                tup[1] = value
                return
                
        self.arr.append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for tup in self.arr:
            if tup[0] == key:
                return tup[1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for idx, tup in enumerate(self.arr):
            if tup[0] == key:
                self.arr.pop(idx)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# 2nd solution (faster, but use more space)
# time complexity: O(1), every operation is constant time
# space complexity: O(1), fixed size of array
class MyHashMap2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [0] * 1000001

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.arr[key] = value + 1

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.arr[key] - 1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.arr[key] = 0
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)