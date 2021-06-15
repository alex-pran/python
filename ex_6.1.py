#ex 6.1


print("\n\n======================= 6.1 ===================")

human = {'first_name': 'john', 'last_name': 'doe', 'age': 38, 'city': 'atlanta'}
print(human['first_name'].title())
print(human['last_name'].title())
print(human['age'])
print(human['city'].title())

print("\n\n======================= 6.2 ===================")

names = {'john': 5, 'ken': 6, 'tom': 1, 'ella': 8, 'rita': 12}
favorite_number = names['john']
favorite_number2 = names['ken']
favorite_number3 = names['tom']
favorite_number4 = names['ella']
favorite_number5 = names['rita']

print(f"John's Favorite number is: {favorite_number}")
print(f"Ken's Favorite number is: {favorite_number2}")
print(f"Tomas Favorite number is: {favorite_number3}")
print(f"Ella's Favorite number is: {favorite_number4}")
print(f"Rota Favorite number is: {favorite_number5}")

for key, value in names.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\n\n======================= 6.3 ===================")


for key, value in human.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("\n\n ==================== 6.4 ======================")

print("\n\n ==================== 6.7 ======================")

people = {'artkatty':{'firstname': 'katty', 'lastname': 'shishkina', 'location': 'brooklyn'},
           'apranitchii':{'firstname': 'alexandr', 'lastname': 'pranitchii', 'location': 'brooklyn'},
          'jdoe': {'firstname': 'john', 'lastname': 'doe', 'age': 24, 'location': 'atlanta'}}

for usernames, users_info in people.items():
    print(f"\nUsername: {usernames}")
    fullysh_name = f"{users_info['firstname']} {users_info['lastname']}"
    locations = f"{users_info['location']}"
    print(f"\tFull name: {fullysh_name.title()}")
    print(f"\tLocation: {locations.title()}")


print("\n\n ==================== 6.8 ======================")

pets = {'name1': {'cat': 'fox', 'bridal': 'scotisch', 'owner': 'KA'},
        'name2': {'cat': 'fluffy', 'bridal': 'empty', 'owner': 'KA'}}

for pet, pets_info in pets.items():
    print(f"Pet: {pet}")
    full_info = f"{pets_info['cat']} {pets_info['bridal']} {pets_info['owner']}"
    print(f"About pet: {full_info}")

