moves = input()

ball_location = 1

for move in moves :
	if (move=='A') and (ball_location==1) :
		ball_location = 2
	elif (move=='A') and (ball_location==2) :
		ball_location = 1
	elif (move=='B') and (ball_location==2) :
		ball_location = 3
	elif (move=='B') and (ball_location==3) :
		ball_location = 2
	elif (move=='C') and (ball_location==3) :
		ball_location = 1
	elif (move=='C') and (ball_location==1) :
		ball_location = 3

print(ball_location)