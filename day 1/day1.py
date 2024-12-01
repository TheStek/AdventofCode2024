with open('input.txt', 'r') as f:
	data = f.read().splitlines()

def part1(data):
	list1 = [int(x.split(' ')[0]) for x in data]
	list2 = [int(x.split(' ')[-1]) for x in data]

	return sum(map(lambda x: abs(x[0] - x[1]), zip(sorted(list1), sorted(list2))))

def part2(data):
	list1 = [int(x.split(' ')[0]) for x in data]
	list2 = [int(x.split(' ')[-1]) for x in data]

	l2_counts = {}

	for item in list2:
		if item in l2_counts.keys():
			l2_counts[item] += 1
		else:
			l2_counts[item] = 1

	def get_similarity(x):
		appearances = l2_counts.get(x)
		if appearances is None:
			return 0
		return x*appearances

	return sum(map(get_similarity, list1))

print(part1(data))
print(part2(data))