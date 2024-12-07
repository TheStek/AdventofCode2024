import time
import os
import copy

def add_coordinates(x, y):
    return (x[0] + y[0], x[1] + y[1])

def parse_map(map_string):
    parsed_map = list(map(lambda x: [y for y in x], map_string.split('\n')))
    if parsed_map[-1] == ['']:
        parsed_map = parsed_map[:-1]
    return parsed_map


class Guard:
    directions = '^>V<'
    direction_movement = {'^': (-1, 0),
                     '>': (0, 1),
                     '<': (0, -1),
                     'V': (1, 0)}


    def __init__(self, parsed_map):
        self.map = copy.deepcopy(parsed_map)
        self.path = [self.get_starting_postion()]
        self.positions = set()
        self.positions.add(self.get_position_and_direction())
        self.out_of_bounds = False
        self.in_loop = False

    def get_position_and_direction(self):
        return (self.path[-1][0], self.path[-1][1], self.current_direction)


    def get_location_value(self, row, col):
        if row < 0:
            return  None

        if col < 0:
            return None
        try:
            return self.map[row][col]
        
        except:
            return None
        
        
    def set_location_value(self, row, col, value):
        self.map[row][col] = value
        

    def get_starting_postion(self):
        for row in range(len(self.map)):
            for col in range(len(self.map[0])):
                value = self.get_location_value(row, col)
                if value in self.directions:
                    self.current_direction = self.get_location_value(row, col)
                    return (row, col)
                

    def turn(self):
        self.current_direction = self.directions[(self.directions.index(self.current_direction) + 1)%len(self.directions)]


    def advance(self):
        next_square = add_coordinates(self.path[-1], self.direction_movement.get(self.current_direction))
        next_square_value = self.get_location_value(*next_square)
        
        if next_square_value is None:
            self.out_of_bounds = True
            return
        
        elif next_square_value !=  '#':
            self.set_location_value(*self.path[-1], 'X')
            self.set_location_value(*next_square, self.current_direction)
            self.path.append(next_square)
            
        else:
            self.turn()
            self.map[self.path[-1][0]][self.path[-1][1]] = self.current_direction
            self.path.append(self.path[-1])
        

        current_position  = self.get_position_and_direction()
        if current_position in self.positions:
            self.in_loop = True
            return
        
        self.positions.add(self.get_position_and_direction())
            

    def print_map(self):
        for row in self.map:
            print(''.join(row))
        print()


    def perform_route(self, display = False):
        while not (self.out_of_bounds or self.in_loop):
            if display: os.system('cls')
            if display: self.print_map()
            if display: print(self.get_position_and_direction())
            self.advance()
            if display: time.sleep(0.1)
            

        return self.path



test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

test2 = """.##..
....#
.....
.^.#.
....."""


with open('input.txt', 'r') as f:
	data = f.read()


def part1(data):
    parsed_map = parse_map(data)

    s = time.time()
    guard = Guard(parsed_map)

    print(len(set(guard.perform_route())))
    print(time.time() - s)



def part2(data):
    loops = []
    parsed_map = parse_map(data)

    guard = Guard(parsed_map)
    path = set(guard.perform_route())
    to_check = len(path)
    i = 0
    for row, col in path:
        i+= 1
        
        if parsed_map[row][col] != '.':
            continue
        
        new_map = copy.deepcopy(parsed_map)
        new_map[row][col] = '#'

        guard = Guard(new_map)
        guard.perform_route()
        if guard.in_loop:
            loops.append((row, col))

        print(f'Checking {i}/{to_check}, {len(loops)} loops', end = '\r')
    print()
    return len(loops)

print(part2(data))
