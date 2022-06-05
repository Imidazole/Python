from itertools import cycle

s = input("Введите элементы цикла, разделённые пробелом:\n")

l = s.split()

i = 0

for it in cycle(l):
	print(it)
	i += 1
	if i > 1000:
		break
