def clean_email(address) :
	index_plus = address.find("+")
	if index_plus != -1 :
		index_at = address.find("@")
		address = address[:index_plus]+address[index_at:]

	index_at = address.find("@")
	no_dot = ''
	i = 0
	while i<index_at :
		if address[i]!="." :
			no_dot += address[i]
		i = i+1
	cleaned = (no_dot+address[index_at:]).lower()
	return cleaned

for _ in range(10) :
	n = int(input())
	addresses = set()
	for i in range(n) :
		address = input()
		address = clean_email(address)
		addresses.add(address)
	print(len(addresses))