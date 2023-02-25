for _ in range(10) :
	costs = [12, 10, 7, 5]

	trip_cost = int(input())
	year_per = input().split()
	brunch = int(input())

	for i in range(len(year_per)) :
		year_per[i] = float(year_per[i])

	year_students = []
	for i in range(len(year_per)) :
		year_students.append(int(brunch*year_per[i]))

	remain = brunch-sum(year_students)
	max_year = max(year_students)
	max_index = year_students.index(max_year)
	year_students[max_index] += remain

	total_raised = 0
	for i in range(len(year_students)) :
		total_raised += year_students[i]*costs[i]

	if (total_raised/2)<trip_cost :
		print("YES")
	else :
		print("NO")