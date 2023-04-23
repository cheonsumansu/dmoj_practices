width = int(input())
cheese = int(input())

satisfaction = ""
if width==3 and cheese>=95 :	#at least = 이상
	satisfaction = "absolutely"
elif width==1 and cheese<=50 :	#at most = 이하
	satisfaction = "fairly"
else :
	satisfaction = "very"

print("C.C. is " + satisfaction + " satisfied with her pizza.")
	