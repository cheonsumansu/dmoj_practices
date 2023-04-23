word = ''
words = []
while(word!='quit!') :
	word = input()

	if word=='quit!' :
		break
	elif (len(word)>4) and (word[-2:]=='or') and (word[-3] not in 'aeiouy') :
		words.append(word[:-2]+'our')
	else :
		words.append(word)


for i in range(len(words)) :
	print(words[i])