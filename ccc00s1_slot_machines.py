chips = int(input())
first = int(input())
second = int(input())
third = int(input())

play_times = 0
machine = 1

while(chips!=0) :
	chips -= 1
	if (machine==1) :
		first += 1
		if (first==35) :
			first = 0
			chips += 30
	
	if (machine==2) :
		second += 1
		if (second==100) :
			second = 0
			chips += 60

	if (machine==3) :
		third += 1
		if (third==10) :
			third = 0
			chips += 9

	play_times += 1
	machine += 1
	if (machine==4) :
		machine = 1

print("Martha plays " + str(play_times) + " times before going broke.")