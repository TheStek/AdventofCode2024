with open('input.txt', 'r') as f:
	data = f.read().splitlines()

test_data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split('\n')

def check_safety(report):
    difs = [y[0] - y[1] for y in zip(report, report[1:])]

    min_dif = min(map(abs, difs))
    max_dif = max(map(abs, difs))
    if min_dif < 1:
        return False
    if max_dif > 3:
            return False
    

    sign = lambda x: 1 if abs(x) == x else -1

    if abs(sum(map(sign, difs))) != len(difs):
        return False
    

    return True


def part1(data):
    reports = list(map(lambda x: [int(y) for y in x.split(' ')], data))
    return len(list(filter(check_safety, reports)))


def part2(data):
    reports = list(map(lambda x: [int(y) for y in x.split(' ')], data))

    safe = 0

    for report in reports:
        if check_safety(report):
            safe += 1
            continue

        for i in range(len(report)):
            temp = report.pop(i)
            if check_safety(report):
                safe += 1
                break
            report.insert(i, temp)

    return safe

print(part1(data))
print(part2(data))


