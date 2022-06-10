fout = open("my_file.txt", "w")

while True:
	inp_str = input("Введите число (для завершения ничего не вводите):\n")
	if inp_str == "":
		break
	fout.write(inp_str + " ")

fout.close()
