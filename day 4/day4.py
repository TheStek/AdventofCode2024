import numpy as np

with open('input.txt', 'r') as f:
	data = f.read()

test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

def count_occurances(string):
    count = 0
    while len(string) >= 4:
        if string[0:4] in ('XMAS', 'SAMX'):
            count += 1
        string = string[1:]

    return count

def part1(data):
    rows = np.array(list(map(list, data.splitlines())))

    columns = rows.T
    flipped = np.fliplr(rows)
    right_diagonals = [list(rows.diagonal(i)) for i in range(-1*rows.shape[1], rows.shape[0])]
    left_diagonals = [list(flipped.diagonal(i)) for i in range(-1*flipped.shape[1], flipped.shape[0])]

    all_strings = []
    all_strings = all_strings + [''.join(x) for x in rows.tolist()]
    all_strings = all_strings + [''.join(x) for x in columns.tolist()]
    all_strings = all_strings + [''.join(x) for x in right_diagonals]
    all_strings = all_strings + [''.join(x) for x in left_diagonals]


    counts = map(count_occurances, all_strings)
    return sum(counts)


def part2(data):
    word_search = data.splitlines()
    rows = len(word_search)
    cols = len(word_search[0])
    count = 0
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if word_search[row][col] != 'A':
                continue

            top_left = word_search[row-1][col-1]
            top_right = word_search[row-1][col+1]
            bot_left = word_search[row+1][col-1]
            bot_right = word_search[row+1][col+1]

            if sorted([top_left, bot_right]) == ['M', 'S'] and sorted([top_right, bot_left]) == ['M', 'S']:
                count += 1

    return count
            
    
print(part1(data))
print(part2(data))