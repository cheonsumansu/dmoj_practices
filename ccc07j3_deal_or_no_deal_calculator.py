number = int(input())
money = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
opened = 0

for i in range(number) :
	opened = (int(input()))
	money[opened-1] = 0

banker = int(input())
avg_money = sum(money)/(10-number)

if (banker>avg_money) :
	print("deal")
else :
	print("no deal")