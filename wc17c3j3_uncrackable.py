password = input()
up = 0
lo = 0
di = 0

if len(password)<8 or len(password)>12 :
	print("Invalid")

else :
	for pw in password :
		if pw.isupper() :
			up += 1

		if pw.islower() :
			lo += 1

		if pw.isdigit() :
			di += 1

	if up>=2 and lo>=3 and di>=1 :
		print("Valid")

	else :
		print("Invalid")