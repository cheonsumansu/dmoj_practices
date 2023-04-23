people = int(input())
infected = int(input())
spreaded = int(input())
day = 0

total_infected = infected
while (people>=total_infected) :
	day += 1
	infected = infected*spreaded
	total_infected += infected

print(day)