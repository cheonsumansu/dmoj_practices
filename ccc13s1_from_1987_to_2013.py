def after_distinct_year(year) :
	after_year = str(year)
	for yr in after_year :
		if after_year.count(yr)>1 :
			return False
	return True


# MAIN
year = int(input())+1

while not after_distinct_year(year) :
	year += 1

print(year)