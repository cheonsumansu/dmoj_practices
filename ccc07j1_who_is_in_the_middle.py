first = int(input())
second = int(input())
third = int(input())

if (second>first and first>third) or (second<first and first<third) :
	print(first)
elif (first>second and second>third) or (first<second and second<third) :
	print(second)
else :
	print(third)