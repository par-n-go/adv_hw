countries = {
    'Ukraine':'Kiev',
    'Switzerland':'Bern',
    'France':'Paris',
    'Germany':'Berlin',
}
countries_list = ['Ukraine', 'France', 'Belgium', 'Austria']

for country in countries_list:
    if country in countries:
        print (countries[country])