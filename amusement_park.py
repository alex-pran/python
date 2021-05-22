age = 25

if age <= 4:
    print("Your are admission cost is $0")

elif age < 18:
    print("Your are admission cost is $25")

elif age <= 25:
    print("Your are admission is $30")

else:
    print("Your are admission cost is $40")

print("\n\n================= short version =================")

age = int(input())
if age <= 4:
    price = 0

elif age <= 18:
    price = 15

elif age <= 25:
     price = 30

elif age < 65:
    price = 40

elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}")