number = int(input())
decks = [ [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
		[4, 4, 4, 4, 4, 4, 4, 4, 16, 4] ]

cards = []
for i in range(number) :
	integer = int(input())
	cards.append(integer)

for i in range(len(cards)) :
	decks[1][cards[i]-2] -= 1

diff = 21-sum(cards)

if diff>11 :
	print("VUCI")
else :
	left_decks = 0
	for i in range(diff-1) :
		left_decks += decks[1][i]

	right_decks = 0
	for i in range(diff-1, 10) :
		right_decks += decks[1][i]


	if left_decks>right_decks :
		print("VUCI")
	else :
		print("DOSTA")
