#마을 사람들은 저녁마다 큰 불주위에 모여서 노래를 부름
#저명한 멤버는 바드, 매일 저녁 바드가 있다면 주민들이 첨듣는 새로운 노래를 부르고 다른 노래는 안부름
#이때 바드가 없다면 다른 주민들이 주민들이 알고있는 노래들을 전부 부르며 노래를 교환
#E만큼 연속 참여한 주민 목록이 있다면 그 기간동안 모든 주민들이 아는 노래를 출력

#N = 주민 수, 2<=N<=100, 1은 바드
#E = 저녁 날짜수, 1<=E<=50
#K = 각 E저녁에 참석한 주민목록, 2<=K<=N
#하루에 두번 나타나는 주민은 없고 바드는 저녁날짜동안 최소 한번은 나온다
#바드를 포함하여 공개된 노래를 전부 알고있는 모든 주민을 오름차순으로 한글자씩 출력


num_villagers = int(input())
num_evenings = int(input())
knows = []
for i in range(num_evenings) :
	k = input().split()
	for j in range(1, int(k[0])+1) :
		k[j] = int(k[j])
	num_presented = k[0]
	presented = set(k[1:])
	
	if 1 in presented :
		knows.append(presented)
	else :
		for prnt in presented :
			for j in range(len(knows)) :
				if prnt in knows[j] :
					knows[j] = knows[j].union(presented)

results = set()
for i in range(len(knows)-1) :
	results = knows[i].intersection(knows[i+1])
	knows[i+1] = results
results = sorted(list(results))
print(*results, sep="\n")
