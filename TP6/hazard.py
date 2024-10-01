import random

L=[random.randint(0,10) for i in range(4)]
print(L)
for i in range(10):print(random.choice(L))
