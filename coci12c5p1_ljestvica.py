#맨 첫 음조갯수가 c, f, g가 많으면 c마이너, a, d, e가 많으면 a마이너
#아놔 c랑 a 갯수가 같으면 메인음조가 아니라 전체음조 마지막으로 판단하는 거였음

lines = input()
tones = ''
c_counts = 0
a_counts = 0

for i in range(len(lines)) :
	if (i==0) or (lines[i-1]=='|') :
		tones += lines[i]

for i in range(len(tones)) :
	if (tones[i]=='C') or (tones[i]=='F') or (tones[i]=='G') :
		c_counts += 1
	if (tones[i]=='A') or (tones[i]=='D') or (tones[i]=='E') :
		a_counts += 1

if c_counts<a_counts :
	print("A-mol")
elif c_counts>a_counts :
	print("C-dur")
else :
	if (lines[-1]=='C') or (lines[-1]=='F') or (lines[-1]=='G') :
		print("C-dur")
	else :
		print("A-mol")