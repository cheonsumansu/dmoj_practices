number = int(input())

position = []
for i in range(number) :
	position.append(int(input()))

position.sort()

size = []
for i in range(1, number-1) :
	left = (position[i]+position[i-1])/2
	right = (position[i+1]+position[i])/2
	size.append((right-left))

print(min(size))