import re

test_data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
test_data_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open('input.txt', 'r') as f:
	data = f.read()

def part1(data):
    muls = re.findall(r'(mul\((\d{1,3}),(\d{1,3})\))', data)
    return sum(map(lambda x: int(x[1]) * int(x[2]), muls))

def part2(data):
    muls = []
    dontsplit = data.split("don't()")
    
    for i in range(len(dontsplit)):
        section = dontsplit[i]
        if i==0:
            muls.append(section)
            continue

        dosplit = section.split('do()')
        muls.append(''.join(dosplit[1:]))    

    return part1(''.join(muls))


print(part1(data))
print(part2(data))