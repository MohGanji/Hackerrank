def ransom_note(mag, ransom):
	for i in ransom:
		try:
			if mag[i] >= 1:
				mag[i] -= 1
			else:
				return False
		except(KeyError):
			return False
	return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')

mag = {}
for i in magazine:
	try:
		mag[i] += 1
	except(KeyError):
		mag[i] = 1

answer = ransom_note(mag, ransom)
print "Yes" if answer else "No"


