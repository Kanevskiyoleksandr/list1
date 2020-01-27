import random

list = []
list_size = random.randint (1, 20)
for _ in range(list_size):
    list.append(random.randint(1,10))
del list [-1]
print(list)
