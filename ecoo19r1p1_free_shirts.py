for _ in range(10) :
	shirts, events, days = input().split()
	shirts = int(shirts); events = int(events); days = int(days)
	reset_shirts = shirts

	evnt = input().split()
	event_days = []
	for i in range(events) :
		event_days.append(int(evnt[i]))

	laundry = 0
	number = 1
	while (number<=days) :
		if shirts==0 :
			shirts = reset_shirts
			laundry += 1
	
		for i in range(len(event_days)) :
			if number==event_days[i] :
				shirts += 1
				reset_shirts += 1

		shirts -= 1
		number += 1


	print(laundry)
		