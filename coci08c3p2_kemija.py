in_lines = input()
de_lines = ''

i = 0
while (i<len(in_lines)) :
	de_lines += in_lines[i]

	if (in_lines[i] in 'aeiou') :
		i = i+3
	else :
		i += 1

print(de_lines)