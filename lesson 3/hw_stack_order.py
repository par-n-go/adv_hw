class Stack():

    main_stack = []

    def __str__(self):
        stack_name = ''
        for item in self.main_stack:
            stack_name += str(item) + '; '
        return stack_name


    def push(self, element):
        self.main_stack.append(element)
        return element

    def pop(self):
        element = self.main_stack.pop()
        return element


class Order():
    main_order = []
    def __str__(self):
        order_name = ''
        for item in self.main_order:
            order_name += str(item) + '; '
        return order_name

    def push(self, element):
        self.main_order.insert(0,element)
        return element

    def pop(self):
        element = self.main_order.pop()
        return element


# stack example
print('-'*80)
print('Пример стека')
new_stack = Stack()
print (new_stack)

new_stack.push(1)
new_stack.push(2)
new_stack.push(3)

print (new_stack)

print (new_stack.pop())
print (new_stack)


# order example
print('-'*80)
print('Пример очереди')
new_order = Order()
print (new_order)

new_order.push(1)
new_order.push(2)
new_order.push(3)

print (new_order)

print (new_order.pop())
print (new_order)
