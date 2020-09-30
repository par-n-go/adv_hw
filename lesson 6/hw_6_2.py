class Dictionary():

    def __init__(self, **kwargs):
        print (kwargs)
        self._dict = dict()
        self.position = 0

    def __str__(self):
        display = ''
        for key, value in self._dict.keys():
            display += f"'{str(key)}':'{str(value)}',"
        return display

#new_dict = (test1 = 'testik', 1='2', '2'='test', 3=4)
dict1 = Dictionary(one = 'testik', two='2', three = 'test', four=4, )

print (dict1)