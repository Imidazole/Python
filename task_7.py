def cap(s):
	return s[0].upper() + s[1:]

def cap_exp(s):
	arr = list(map(cap, s.split()))
	return " ".join(arr)

s = input("Введите строку:\n")

print(cap_exp(s))
