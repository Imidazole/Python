fin = open("my_file.txt", "r")

i = 0

while True:
	f_line = fin.readline()
	if not f_line:
		break
	n = len(f_line.split())
	i += 1
	print(f"В {i}-й строке {n} слов.")

print(f"В файле {i} строк")

fin.close()
