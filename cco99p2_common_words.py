def invert_dictionary(dict) :
	inverted = {}
	for key in dict :
		temp = dict[key]
		if temp in inverted :
			inverted[temp].append(key)
		else :
			inverted[temp] = [key]
	return inverted


def add_suffixed(num_index) :	#접미사 추가
	s = str(num_index)
	if s[-1]=="1" and s[-2:]!="11" :
		return s+"st"
	elif s[-1]=="2" and s[-2:]!="12" :
		return s+"nd"
	elif s[-1]=="3" and s[-2:]!="13" :
		return s+"rd"
	else :
		return s+"th"


def most_common_words(num_to_words, k) :
	nums = list(num_to_words.keys())
	nums.sort(reverse = True)
	total = 0
	i = 0
	done = False
	while i<len(nums) and not done :
		num = nums[i]
		if total+len(num_to_words[num])>=k :
			done = True
		else :
			total += len(num_to_words[num])
			i += 1
	
	if total==(k-1) and i<len(nums) :
		return num_to_words[nums[i]]
	else :
		return []



num = int(input())
results_index = []
results_words = []
for _ in range(num) :
	num_words, num_index = input().split()
	num_words = int(num_words)
	num_index = int(num_index)
	results_index.append(num_index)
	
	words_to_num = {}
	for i in range(num_words) :
		word = input()
		if not word in words_to_num :
			words_to_num[word] = 1
		else :
			words_to_num[word] = words_to_num[word]+1

	num_to_words = invert_dictionary(words_to_num)
	words = most_common_words(num_to_words, num_index)
	results_words.append(words)

for i in range(num) :
	print(f"{add_suffixed(results_index[i])} most common word(s):")
	for word in results_words[i] :
		print(word)
	print()
