def solution1(raw):
	return sum(b > a for a, b in zip(raw, raw[1:]))

def solution2(raw):
	windows = [ sum(raw[i:i+3]) for i in range(0, len(raw)) ]
	return solution1(windows)

with open('input_kels.txt', 'r') as file:
	raw = list(map(int, file.readlines()))
	print( solution1(raw) )
	print( solution2(raw) )
