def fn(s):
	filt_s = ''
	for char in s:
		if char.isalnum():
			filt_s += char.lower()
	first = 0
	second = len(filt_s) - 1 #indexing less than 1
	print(filt_s)	
	while True:
		print(f'{filt_s[first]} --- {filt_s[second]}')
		if first == second or second < first:
			break
		if filt_s[first] != filt_s[second]:
			return False
		first += 1
		second -= 1
	return True


fn("tab a cat")
