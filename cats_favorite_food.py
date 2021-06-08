favorite_food = {'fluffy':['chicken','tuna'], 'fox':['tuna','treats'],
                 'charlie':['salmon'],'tom':['mouse','cheese']}
for name,foods in favorite_food.items():
    print(f"\n{name.title()} it favorite food:")
    for food in foods:
        print(f"\t{food.title()}")


print("\n\nffffffffffffffff =============== fffffffffffffffff")

money = {'usa':['usd'], 'russia':['rub'], 'italy':['euro']}

for name, country in money.items():
    print(f"\n{name.title()} - bills of country:")
    for moneys in country:
        print(f"\t{moneys}")


print("\n\nffffffffffffffff =============== fffffffffffffffff")

brand_cars = {'honda':['accord','civic','fit','pilot','odissey'],
        'toyota':['corolla','camry','avalon','rav4'],
        'nissan':['sentra','altima','maxima','rogue'],
        'subaru':['impreza','legacy','brz','forester','outback']}

for name,model in brand_cars.items():
    print(f"\n{name.title()} have many models:")
    for models in model:
        print(f"{models}")
