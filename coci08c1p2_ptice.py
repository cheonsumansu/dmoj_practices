question = int(input())
answer = input()

adrian = 'ABC'*int( (question/3) +1)
bruno = 'BABC'*int( (question/4) +1)
goran = 'CCAABB'*int( (question/6) +1)
ad_count = 0
br_count = 0
go_count = 0

for i in range(question) :
	if (answer[i]==adrian[i]) :
		ad_count += 1
	if (answer[i]==bruno[i]) :
		br_count += 1
	if (answer[i]==goran[i]) :
		go_count += 1
			
max_count = max(ad_count, br_count, go_count)
print(max_count)
if (max_count==ad_count) :
	print("Adrian")
if (max_count==br_count) :
	print("Bruno")
if (max_count==go_count) :
	print("Goran")
