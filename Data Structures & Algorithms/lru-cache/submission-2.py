from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cch = {}
        self.order = deque()

    def get(self, key: int) -> int:
        if key not in self.cch:
            return -1

        # Move key to most-recently-used position
        self.order.remove(key)
        self.order.append(key)

        return self.cch[key]

    def put(self, key: int, value: int) -> None:

        # If key already exists, remove its old position
        if key in self.cch:
            self.order.remove(key)

        # If cache is full, remove LRU key
        elif len(self.cch) == self.cap:
            k = self.order.popleft()
            del self.cch[k]

        # Add/update key as most recently used
        self.cch[key] = value
        self.order.append(key)


# from collections import deque
# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cch = {}
#         self.order = deque() 
#         # self.top = -1

#     def get(self, key: int) -> int:
#         print(self.order, self.cch)
#         if(key in self.cch):
#             return self.cch[key]
#         else:
#             return -1

#     def put(self, key: int, value: int) -> None:
#         # if(len(self.cch) == 0):
#         #     self.top = key
#         if(len(self.cch) == self.cap):
#             k = self.order.popleft()
#             self.cch.pop(k)
#         self.order.append(key)
#         self.cch[key] = value
#         return None

        

