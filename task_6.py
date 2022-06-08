import re

def parse_string(s):
	m = re.compile(r"(\d+)\(([а-я]+)\)")

	p = re.finditer(m, s)
	res = 0
	
	for i in p:
		res += int(i.group(1))
	
	return res

def get_name(s):
	m = re.compile(r"([a-я]+)\:")
	p = re.match(m, s)
	return p.group(1)

fin = open("my_file.txt", "r")
d = dict()

while True:
	f_line = fin.readline()
	if not f_line:
		break
	val = parse_string(f_line)
	nm = get_name(f_line)
	d[nm] = val

fin.close()

print(d)
