fin = open("my_inp_file.txt", "r")
fout = open("my_outp_file.txt", "w")

d = \
	{
		"one" : "один",
		"two" : "два",
		"three" : "три",
		"four" : "четыре",
		"five" : "пять",
		"six" : "шесть",
		"seven" : "семь",
		"eight" : "восемь",
		"nine" : "девять"
	}

while True:
	f_line = fin.readline()
	if not f_line:
		break
	arr = f_line.split()
	arr[0] = d[arr[0]]
	fout.write(" ".join(arr) + "\n")

fin.close()
fout.close()
