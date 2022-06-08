fout = open("my_file.txt", "w")

inp_str = " "

while True:
	inp_str = input("Введите строку:\n")
	if inp_str == "":
		break
	fout.write(inp_str + "\n")

fout.close()
