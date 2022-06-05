s = input("Введите список чисел, разделённых пробелами:\n")

l = list(map(int, s.split()))

l_s = [el for el in l if l.count(el) == 1]

print("Список неповторяющихся элементов:", l_s, sep = "\n")
