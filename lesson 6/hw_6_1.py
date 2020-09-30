class List():

    def __init__(self, *args):
        self._list = list(args)
        self.position = 0

    def __str__(self):
        return f"[{', '.join(str(x) for x in self._list)}]"

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < len(self._list):
            result = self._list[self.position]
            self.position += 1
            return result
        else:
            self.position = 0
            raise StopIteration()

    def pop(self):
        result = self._list.pop()
        #del self._list[-1]
        return result

    def append(self, value):
        self._list.append(value)

    def insert(self, key, value):
        if key < len(self._list) and key >= 0:
            self._list.insert(key, value)
        else:
            raise KeyError()

    def remove(self, value):
        self._list.remove(value)

    def clear(self):
        self._list.clear()
        self.position = 0

    def __add__(self, other):
        new_list = []
        new_list.extend(self._list)
        new_list.extend(other._list)
        return List(*new_list)


list1 = List(1, 2, 3, 4, 5)
list2 = List(6, 7, 8, 9, 10)

print (list1)

print (list2)

list3 = list1+list2

print (list3)

print (list3.pop())
print (list3.pop())

list3.remove(2)
list3.insert(1, 2)


print (list3)

