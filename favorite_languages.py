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
print('===================================')
for name in favorite_languages.keys():
    print(name.title())

