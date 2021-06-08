user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
user_1 = {'username': 'mascon', 'first': 'enio', 'last': 'domin'}
user_2 = {'username': 'sand', 'first': 'herix', 'last': 'ogrik'}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
users = [user_0, user_1, user_2]

for user in users:
    print(user)

users = []
for users_numbers in range(30):
    new_users = {'username': 'kamato', 'first': 'alexherix', 'last': 'pran'}
    users.append(new_users)

for user in users[:5]:
    print(user)

print("...")
