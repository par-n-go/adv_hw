class Store():
    workers = 0
    sold = 0
    income = 0
    def __init__(self, name, sold):
        self.name = name
        self.sold = sold
        Store.sold += sold
    def sell_product(self, price):
        self.sold += 1
        Store.sold += 1
        self.income += price

    def add_worker(self, workers):
        self.workers += workers

    def __str__(self):
        return "{} sold {} product for total income of {} dollars with {} workers".format(self.name, self.sold, self.income, self.workers)

silpo = Store('Silpo', 10)
silpo.sell_product(1000)
silpo.add_worker(2)
print (silpo)

ashan = Store('Ashan', 50)
ashan.sell_product(40000)
ashan.sell_product(30000)
ashan.add_worker(50)
print (ashan)

print (f'Total sold by all stores = {Store.sold}')
