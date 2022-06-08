fout = open("my_file.txt", "r")

f_line = fout.readline()

ar = f_line.split()
s = sum(map(int, ar))

print(s)
