from collections import defaultdict
from typing import List, Tuple
from aoc import AocData
from termcolor import colored
import colorama

SYM_EMPTY = "."
SYM_GEAR = "*"

colorama.init()

def find_adjacents(start_x, end_x, base_y, grid):
    adjacents = []

    for y in range(base_y - 1, base_y + 2):
        for x in range(start_x - 1, end_x + 1):
            try:
                sym = grid[y][x]
            except IndexError:
                continue

            if sym != SYM_EMPTY and not sym.isnumeric():
                adjacents.append(sym)
            
            if sym == SYM_GEAR:
                gears[y][x].append(int(grid[base_y][start_x:end_x]))
    
    return adjacents


def find_numbers_with_adajcents(y, grid) -> Tuple[int, List[str]]:
    results = []
    start_x = None
    line = grid[y]
    for x, s in enumerate(line):
        if s.isnumeric() and start_x is None:
            start_x = x 
        
        if not s.isnumeric() and start_x is not None:
            results.append((int(line[start_x:x]), find_adjacents(start_x, x, y, grid)))
            if len(results[-1][1]) > 0:
                color = "green"
            else:
                color = "red"
            pretty_grid[y] += colored(line[start_x:x], color)
            start_x = None
        
        if not s.isnumeric():
            pretty_grid[y] += colored(s, "white")

    
    # line ends with number
    if start_x is not None:
        results.append((int(line[start_x:]), find_adjacents(start_x, x+1, y, grid)))
        if len(results[-1][1]) > 0:
            color = "green"
        else:
            color = "red"
        pretty_grid[y] += colored(line[start_x:], color)
    return results



data = AocData(3, small=False)
grid = data.lines()
pretty_grid = ["" for l in grid]
debug_results = [[[], 0] for l in grid]
gears = defaultdict(lambda: defaultdict(list))

solution1 = 0
for y in range(0, len(grid)):
    for number, adjacents in find_numbers_with_adajcents(y, grid):
        if len(adjacents) > 0:
            solution1 += number
            debug_results[y][0].append(number)
            debug_results[y][1] += (number)

solution2 = 0
for gearlines in gears.values():
    for gear in gearlines.values():
        if len(gear) == 2:
            solution2 += gear[0] * gear[1]



for l in pretty_grid:
    print(l)

print(solution1)
print(solution2)