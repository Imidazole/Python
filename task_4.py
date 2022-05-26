n = int(input("Введите число:\n"))

max_digit = 0

while(n > 0):
	max_digit = max(max_digit, n % 10)
	n //= 10

print("Наибольшая цифра:", max_digit, sep = "\n")
