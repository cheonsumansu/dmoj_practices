distance = input().split()
for i in range(len(distance)) :
	distance[i] = int(distance[i])

distance_a = []
for i in range(len(distance)+1) :
	distance_a.append(sum(distance[:i]))

distance_b = []
for i in range(len(distance_a)) :
	dt_b = []
	for j in range(len(distance_a)) :
		dt_b.append(abs(distance_a[j]-distance_a[i]))
	distance_b.append(dt_b)

for i in range(len(distance_b)) :
	for j in range(len(distance_b[i])) :
		print(distance_b[i][j], end=' ')
	print()