from sys import argv

perf, wage, bonus = map(int, argv[1:])

salary = perf * wage + bonus

print("Заработная плата:", salary, sep = "\n")
