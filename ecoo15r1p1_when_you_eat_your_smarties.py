for _ in range(10) :
	color = ''
	
	orange = 0
	blue = 0
	green = 0
	yellow = 0
	pink = 0
	violet = 0
	brown = 0
	red = 0

	while(color!='end of box') :
		color = input()
	
		if color=='orange' :
			orange += 1
		elif color=='blue' :
			blue += 1
		elif color=='green' :
			green += 1
		elif color=='yellow' :
			yellow += 1
		elif color=='pink' :
			pink += 1
		elif color=='violet' :
			violet += 1
		elif color=='brown' :
			brown += 1
		elif color=='red' :
			red += 1
	
	
	count = orange//7 + blue//7 + green//7 + yellow//7 + pink//7 + violet//7 + brown//7
	if orange!=0 and orange%7!=0 :
		count += 1
	if blue!=0 and blue%7!=0 :
		count += 1
	if green!=0 and green%7!=0 :
		count += 1
	if yellow!=0 and yellow%7!=0 :
		count += 1
	if pink!=0 and pink%7!=0 :
		count += 1
	if violet!=0 and violet%7!=0 :
		count += 1
	if brown!=0 and brown%7!=0 :
		count += 1
	
	print(count*13 + red*16)
	
	