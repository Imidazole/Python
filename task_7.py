import json

companies = dict()
sum_profit = 0

with open("my_file.txt", "r") as fin:
	while True:
		f_line = fin.readline()
		if not f_line:
			break
		ar = f_line.split()
		profit = int(ar[2]) - int(ar[3])
		sum_profit += profit
		companies[ar[0]] = profit

av_profit = sum_profit / len(companies)
ap = dict([("average_profit", av_profit)])

res = [companies, ap]

with open("my_file.json", "w") as fout:
	json.dump(res, fout)
