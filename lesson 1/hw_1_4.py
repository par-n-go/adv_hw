deposit = 150
years = 3
percent = 5

def bank(deposit,years, percent):
    for i in range(years):
        deposit += deposit/100*percent
    return deposit

print (bank(deposit, years, percent))