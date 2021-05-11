cars = ['bmw', 'toyota', 'audi', 'honda']

cars.sort()
print(cars)

print("--------------------------------------")

cars = ['bmw', 'toyota', 'audi', 'honda']
cars.sort(reverse=True)
print(cars)

print("--------------------------------------")

cars = ['bmw', 'toyota', 'audi', 'honda']

print("Here is original list: ")
print(cars)                        #Here is original list: ['bmw', 'toyota', 'audi', 'honda']

print("\nHere is a sorted list: ")
print(sorted(cars))                #Here is a sorted list: ['audi', 'bmw', 'honda', 'toyota']
print("---------------------")
print("\nHere is a sorted revers list: ")
print(sorted(cars, reverse=True))  #Here is a sorted reverse list: ['toyota', 'honda', 'bmw', 'audi']

print("\nHere is original list again: ")
cars.reverse
print(cars)

print("----------------------------")

num = ['3','7','1','0','4','2','9','5','8','6']
print(num)

num.reverse()
print(num)

print(sorted(num))
print(sorted(num,reverse=True))
num.reverse()

