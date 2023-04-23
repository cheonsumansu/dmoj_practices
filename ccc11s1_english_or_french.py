num = int(input())
s_counts = 0
t_counts = 0
for i in range(num) :
	lines = input()

	for j in range(len(lines)) :
		if lines[j]=='s' or lines[j]=='S' :
			s_counts += 1
		if lines[j]=='t' or lines[j]=='T' :
			t_counts += 1

if s_counts<t_counts :
	print("English")
else :
	print("French")