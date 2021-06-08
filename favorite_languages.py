favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
language = favorite_languages['sarah'].title()
language2 = favorite_languages['jen'].title()
language3 = favorite_languages['edward'].title()
language4 = favorite_languages['phil'].title()
print(f"Sarah's favorite languge is {language}.")
print(f"Jen's favorite languge is {language2}.")
print(f"Phil's favorite languge is {language4}.")
print(f"Edward favorite languge is {language3}.")

for key, value in favorite_languages.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")


for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")
print('\n\n===================================')


for name in favorite_languages.keys():
    print(name.title())
print('\n\n===================================')
for name in favorite_languages:
    print(name.title())
print('\n\n=============2222222======================')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

    if 'erin' not in favorite_languages.keys():
        print("\t\nErin, please take our poll")

print('\n\n================22222222===================')

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print('\n\n===================================')

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    
print("\n\n=============================")

for language in set(favorite_languages.values()):
    print(language.title())

print("\n\n=============================")
print("\n\n=============================")
print("\n\n=============================")
print("\n\n=============================")


favorite_languages = {'jen':['python', 'ruby'],
                      'sarah':['c'], 'edward':['ruby', 'go'],
                      'phil':['python', 'haskell'],}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")