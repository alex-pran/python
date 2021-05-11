

bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)
print(bicycle)
print(bicycle[2])
print(bicycle[-1].title())
print(bicycle[-2].title())
print(bicycle[-3].title())
print(bicycle[-4].title())


message = f"My first bicycle was {bicycle[2].title()}"
print(message)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
# izmenennie "honda na ducati"
motorcycles[0] = 'ducati'
print(motorcycles)

#добавление в список в конце (*****.append)

motorcycles.append('harley')
motorcycles.append('davidson')
print(motorcycles)

# добавление в список с указанием порядкового номера (****.insert)
# [(0 -) 'ducati', 'honda', (2 -) 'harley', 'yamaha', 'suzuki']
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
motorcycles.insert(2, 'harley')
print(motorcycles)


#удвление из списка при помощи "del"

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0] #delete honda
print(motorcycles)

del motorcycles[1]  #delete suzuki
print(motorcycles)

#------------------------------------

# Удаление элемента с использованием метода pop()
# остается только один последний элемент с именеим
# popped_motorcycle = motorcycles.pop() (davidson)
#

motorcycles = ['honda', 'yamaha', 'suzuki', 'harley', 'davidson']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# сообщение о последнем купленном мотоцикле
motorcycles = ['honda', 'suzuki', 'yamaha']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

#--------------------------------------------------

#Вызов pop() может использоваться для удаления элемента в
# произвольной позиции списка; для этого следует указать индекс
# удаляемого элемента в круглых скобках.


motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(1)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#------------------------------------------------

#Удаление элементов по значению
#метод remove() нужно указать текст в скобках

motorcycles = ['honda', 'yamaha', 'suzuki', 'honda']
print(motorcycles)

motorcycles.remove('honda')
print(motorcycles)

#

#--------------------------------

#00EX:

list_guest = ['gosha', 'kesha', 'vova', 'roma']
print(f"welcome {list_guest[0].title()} to me.")
print(f"welcome {list_guest[1].title()} to me.")
print(f"welcome {list_guest[2].title()} to me.")
print(f"welcome {list_guest[3].title()} to me.")

print(f"\t\t\t\t\t\t\t\t'{list_guest[2].upper()} do not come'")
list_guest[2] = 'kate'
print(f"welcome {list_guest[0].title()} to me.")
print(f"welcome {list_guest[1].title()} to me.")
print(f"welcome {list_guest[2].upper()} to me.")
print(f"welcome {list_guest[3].title()} to me.")


list_guest.insert(0,'sasha')
list_guest.insert(2,'dima')
list_guest.append('kiril')
print(list_guest)

guest6 = list_guest.pop(6)
print(f"Sorry, {guest6}")
guest5 = list_guest.pop(5)
print(f"Sorry, {guest5}")
guest4 = list_guest.pop(4)
print(f"Sorry, {guest4}")
guest3 = list_guest.pop(3)
print(f"Sorry, {guest3}")
guest2 = list_guest.pop(2)
print(f"Sorry, {guest2}")
print(f"welcome, {list_guest}")


print(list_guest)

print("new")

del list_guest[-1]
del list_guest[0]
print(f"empty {list_guest}")





