first = int(input())
second = int(input())
third = int(input())
fourth = int(input())

sum = 0
if (first == 1) :
	sum += 461
elif (first == 2) :
	sum += 431
elif (first == 3) :
	sum += 420
else :
	sum += 0

if (second == 1) :
	sum += 100
elif (second == 2) :
	sum += 57
elif (second == 3) :
	sum += 70
else :
	sum += 0

if (third == 1) :
	sum += 130
elif (third == 2) :
	sum += 160
elif (third == 3) :
	sum += 118
else :
	sum += 0

if (fourth == 1) :
	sum += 167
elif (fourth == 2) :
	sum += 266
elif (fourth == 3) :
	sum += 75
else :
	sum += 0

print("Your total Calorie count is "+str(sum)+".")