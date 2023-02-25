letters = input()
word = 'I'
count = 0

for i in range(len(letters)) :
	if letters[i]=='H' and word=='I' :
		word = 'H'
	elif letters[i]=='O' and word=='H' :
		word = 'O'
	elif letters[i]=='N' and word=='O' :
		word = 'N'
	elif letters[i]=='I' and word=='N' :
		word = 'I'
		count += 1

print(count)