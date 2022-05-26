ss = input("Введите время в секундах:\n")

s = int(ss)

h = (s // 3600)
s = s % 3600

m = (s // 60)
s = s % 60

output = "{0:02d}:{1:02d}:{2:02d}".format(h, m, s)

print("Время в формате 'чч:мм:сс':")
print(output)
