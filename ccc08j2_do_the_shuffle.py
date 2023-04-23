button = 0
playlist = 'ABCDE'

while (button!=4) :
	button = int(input())
	times = int(input())
	
	for i in range(times) :
		if (button==1) :
			playlist = playlist[1:]+playlist[0]
		if (button==2) :
			playlist = playlist[-1]+playlist[:4]
		if (button==3) :
			playlist = playlist[1]+playlist[0]+playlist[2:]
	
for i in range(len(playlist)) :
	print(playlist[i], end=" ")