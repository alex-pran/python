big_river = {'nile': 'egypt', 'amazonka': 'brazil', 'volga': 'russia'}

river_1 = big_river['nile'].title()
river_2 = big_river['amazonka'].title()
river_3 = big_river['volga'].title()

print(f"The Nile runs through {river_1}")
print(f"The Amazonka runs through {river_2}")
print(f"The Volga runs through {river_3}")

for key, value in big_river.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")



print("\n\n================== 9090909 ===================")

users = {'name': 'ron', 'salary': 2000, 'age': 25,'name': 'tom', 'salary': 1000, 'age': 21,'name': 'sarah', 'salary': 2500, 'age': 23,'name': 'mike', 'salary': 3200, 'age': 28, 'name': 'lex', 'salary': 5000, 'age': 41,'name': 'timmy', 'salary': 900, 'age': 19}
def get_data_for_sort(x):
    return x('salary')

sorted(users, key=get_data_for_sort)