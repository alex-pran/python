print("\n\n====================== 5.8 ===================")


names = ['leo', 'kate', 'tom', 'john', 'admin']
for name in names:
    if name == 'admin':
        print(f"Hello {name}, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again")

print("\n\n====================== 5.9 ===================")

hello_admin = ['leo', 'kate', 'tom', 'john', 'admin']
#hello_admin = []
if hello_admin:
    for hello_admins in hello_admin:
        print(f"Added {hello_admins.title()}")
    print("\nReady")
else:
    print("We need to add some users!")


print("\n\n====================== 5.10 ===================")


current_users = ['Leo', 'leo', 'marko', 'rob', 'KATE', 'teddy', 'ronald', 'jeff', 'kate', 'Kate', 'LEO']
new_users = ['Leo', 'kate', 'tom', 'john', 'admin']

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user.title()} use anothe name")
    else:
        print(f"{new_user.title()} you can use this name")

print("\nYou signied")


print("\n\n====================== 5.11 ===================")

numbers = [1,2,3,4,5,6,7,8,9]
for other in numbers:
    if other == 1:
        print(f"\t{other}" + "st")
    elif other == 2:
        print(f"\t{other}" + "nd")
    elif other == 3:
        print(f"\t{other}" + "rd")
    else:
        print(f"{other}" + "th")
