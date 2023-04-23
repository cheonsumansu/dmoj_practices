first_number = int(input())
first_score = []
for i in range(first_number) :
	first_score.append(int(input()))

second_number = int(input())
second_score = []
for i in range(second_number) :
	second_score.append(int(input()))

diff = abs(first_number-second_number)
if first_number>second_number :
	for i in range(diff) :
		second_score.append(0)
if first_number<second_number :
	for i in range(diff) :
		first_score.append(0)

half_score = 0
for i in range(len(first_score)) :
	if first_score[i]<=1440 and first_score[i]!=0 :
		half_score += 1
	if second_score[i]<=1440 and second_score[i]!=0 :
		half_score += 1

turnaround = 0
for i in range(1, len(first_score)) :
	if (first_score[i]==0) or (second_score[i]==0) :
		if (first_score[i]==0) and (first_score[i-1]<second_score[i-1]) :
			turnaround += 1
		elif (second_score[i]==0) and (first_score[i-1]>second_score[i-1]) :
			turnaround += 1
		break
	else :
		if (first_score[i]<second_score[i]) and (first_score[i-1]>second_score[i-1]) :
			turnaround += 1
		elif (first_score[i]>second_score[i]) and (first_score[i-1]<second_score[i-1]) :
			turnaround += 1

print(half_score)
print(turnaround)