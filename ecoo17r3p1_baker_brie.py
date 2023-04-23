for _ in range(10) :
	franchises, days = input().split()
	franchises = int(franchises)
	days = int(days)

	ind_franchise = []
	for i in range(days) :
		goods = input().split()
		for j in range(franchises) :
			goods[j] = int(goods[j])
		ind_franchise.append(goods)

	bonus = 0
	for row in ind_franchise :
		total = sum(row)
		if total%13==0 :
			bonus += (total//13)

	for col in range(franchises) :
		total = 0
		for row in range(days) :
			total += ind_franchise[row][col]
		if total%13==0 :
			bonus += (total//13)

	print(bonus)