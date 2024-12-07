test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

with open('input.txt', 'r') as f:
	data = f.read()


def parse_input(data):
    equations = data.splitlines()
    equations = map(lambda x: x.split(': '), equations)
    equations = map(lambda x: (int(x[0]), list(map(int, x[1].split(' ')))), equations)


    return list(equations)


def check_equation(equation, concat = False):
    answer, operands = equation
    subtotals = [operands.pop(0)]
    while operands:
        
        op = operands.pop(0)
        new_subtotals = []
        for sub in subtotals:
            
            add = sub + op
            if add <= answer:
                new_subtotals.append(add)    
            mult = sub * op
            if mult <= answer:
                new_subtotals.append(mult) 
            if concat:
                conc = int(str(sub) + str(op))
                if mult <= answer:
                    new_subtotals.append(conc)

            
        subtotals = new_subtotals

    return answer in subtotals


def part1(data):
    equations = parse_input(data)

    print(equations[-1])
    valid_equations = filter(check_equation, equations)
    return sum(map(lambda x: x[0], valid_equations))


def part2(data):
    equations = parse_input(data)

    print(equations[-1])
    valid_equations = filter(lambda x: check_equation(x, True), equations)
    return sum(map(lambda x: x[0], valid_equations))


print(part1(data))
print(part2(data))