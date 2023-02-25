space = int(input())
yesterday = input()
today = input()

number = 0

for i in range(len(yesterday)) :
	if yesterday[i]=='C' and today[i]=='C' :
		number += 1

print(number)