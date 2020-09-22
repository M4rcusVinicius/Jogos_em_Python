import random

lista = [random.randrange(1, 4) for n in range(1, 1000)]

print(f"Contagem de 1 :{lista.count(1)}")
print(f"Contagem de 2 :{lista.count(2)}")
print(f"Contagem de 3 :{lista.count(3)}")
print(f"Contagem de 4 :{lista.count(4)}")