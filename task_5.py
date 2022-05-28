ord_list = [7, 5, 2, 1]

new_el = int(input("Введите новый элемент:\n"))

for i, el in enumerate(ord_list):
	if el < new_el:
		ord_list.insert(i, new_el)
		break

print(ord_list)
