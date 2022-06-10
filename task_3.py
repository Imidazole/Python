fin = open("my_file.txt", "r")

sum_salary = 0
i = 0

print("Сотрудники с зарплатой ниже 20000:")

while True:
	f_line = fin.readline()
	if not f_line:
		break
	i += 1
	arr = f_line.split()
	nm = arr[0]
	salary = float(arr[1])
	if salary < 20000:
		print(nm, end = ", ")
	sum_salary += salary

fin.close()

av_salary = sum_salary / i

print(f"Средняя зарплата:\n{av_salary}")
