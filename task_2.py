n = int(input("Введите количество элементов списка:\n"))

l = []

for i in range(n):
	el = input("Введите {}-й элемент списка:\n".format(i+1))
	l.append(el)

ll = len(l) - len(l) % 2

for i in range(0, ll, 2):
	l[i], l[i+1] = l[i+1], l[i]

print(l)
