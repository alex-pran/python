squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# Чтобы сделать код более компактным,
# можно опустить временную переменнуюsquareиприсоединять
# каждое новое значение прямо ксписку:
sq = []
for val in range(1,10):
    sq.append(val**2)
print(sq)

sq1 = [valu**2 for valu in range(1,11)]
print(sq1)



#-------------------------------
print("------------------------------\n\n\n")

                    #ex.4.3

num1 = list(range(1,21))
print(num1)

                  # ex. 4.4
num2 = list(range(1,1_000_000))
print(num2)

for num3 in range(1,1_000_000):
    print(num3)