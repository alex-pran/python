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