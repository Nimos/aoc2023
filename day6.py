import math
from aoc import AocData

data = AocData(6, small=False)

times = [int(x) for x in data.lines()[0].split(" ")[1:] if x]
distances = [int(x) for x in data.lines()[1].split(" ")[1:] if x]

races = zip(times, distances)

# https://www.wolframalpha.com/input?i=x+*+%28t-x%29+%3E+d+solve+for+x
def calc_num_wins(race):
    time, distance = race
    
    lower_bound = 0.5 * (time - math.sqrt(time*time - 4*distance))
    upper_bound = 0.5 * (time + math.sqrt(time*time - 4*distance))

    return math.ceil(upper_bound) - math.floor(lower_bound) - 1

sol = 1
for r in races:
    num_wins = calc_num_wins(r)
    sol *= num_wins


pt2_time = int("".join([str(time) for time in times]))
pt2_distance = int("".join([str(d) for d in distances]))

print(sol)
print(calc_num_wins((pt2_time, pt2_distance)))