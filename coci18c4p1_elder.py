owner = input()
number = int(input())
obey = owner

for i in range(number) :
	wizard1, wizard2 = input().split()
	if wizard2==owner :
		owner = wizard1
		obey += owner
	else :
		continue

print(owner)
print(len(set(obey)))