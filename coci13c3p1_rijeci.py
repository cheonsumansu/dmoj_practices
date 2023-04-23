number = int(input())
a = 1
b = 0
pre_a = 0
pre_b = 0
for i in range(number) :
	pre_a = a
	pre_b = b
	a = pre_b
	b = pre_a+pre_b

print(a, b)