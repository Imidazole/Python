s = input("Введите список чисел, разделённых пробелами:\n")

l = list(map(int, s.split()))

l_s = [l[i] for i in range(1, len(l)) if l[i] > l[i - 1]]

print("Список элементов, больших предыдущего:", l_s, sep = "\n")
