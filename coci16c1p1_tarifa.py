month_data = int(input())
used_month = int(input())
used_data = 0
left = 0

for i in range(used_month) :
	used_data = int(input())
	left = month_data-used_data+left

print(month_data+left)