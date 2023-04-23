#트작인가 뭔가가 주말동안 dmopc문제를 준비했다함
#근데 몇개의 과제가 남음, 트작은 배낭에 N개의 물건이 있다는걸 알게됨
#공간을 아끼려고 아이템을 문자열로 기록, T번의 아이템이 필요한 M개의 과제를 갖고있음(뭔소린지
#만약 트작이 모든 i번째 아이템을 갖고있다면 그는 과제를 i번째 아이템을 끝낼수 있음
#그렇지않으면 낙제라함. 알?빠노? 트작이 몇개의 과제를 할수있는지 결정하래

#1<= N, M, T <= 200
#1<= Si, Ri <=10, S=아이템 문자열 길이

#첫번째 입력줄은 스페이스바로 구분된 N, M
#N: 아이템 갯수, 모든 문자열은 고유함
#M: 과제 갯수, 단락으로 나눠진 업무들의 각각 갯수를 의미(? 설명을 못하겠네
#문제를 해결할수 있는 갯수를 출력하래 이게 뭔소린지..

def check_completed(assignments, items) :
	temp = True
	for assignment in assignments :
		if assignment not in items :
			temp = False
			break
	return temp


num_items, num_assignments = input().split()
num_items = int(num_items)
num_assignments = int(num_assignments)

items = set()
for i in range(num_items) :
	items.add(input())

completed = 0
for i in range(num_assignments) :
	k = int(input())
	assignments = set()
	for j in range(k) :
		assignments.add(input())
	if check_completed(assignments, items) :
		completed += 1

print(completed)