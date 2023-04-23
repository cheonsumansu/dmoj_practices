number = int(input())
streams = []
for i in range(number) :
	streams.append(int(input()))

value = 0
while (value!=77) :
	value = int(input())

	if value==99 :
		split = int(input())
		split_per = int(input())
		left = round(streams[split-1]*(split_per/100))
		right = round(streams[split-1]*((100-split_per)/100))
		streams[split-1] = left
		streams.insert(split, right)
		
	elif value==88 :
		join = int(input())
		combine = streams[join-1]+streams[join]
		streams[join] = combine
		del streams[join-1]


for st in streams :
	print(st, end=' ')