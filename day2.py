
from aoc import AocData


limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def check_possible(game, limits=limits):
    numbers = [number.split(" ") for number in game.split(", ")]
    for number, color in numbers:
        if int(number) > limits[color]:
            return False
    return True

def get_minimums(game, mins=None):
    if not mins:
        mins = {"red": 0, "green": 0, "blue": 0}
    numbers = [number.split(" ") for number in game.split(", ")]
    for number, color in numbers:
        if int(number) > mins[color]:
            mins[color] = int(number)
    
    return mins

def get_product(mins):
    product = 1
    for n in mins.values():
        product *= n if n else 1
    
    return product

data = AocData(2, small=False)

solution1 = 0
solution2 = 0
for line in data.lines():
    game_id = line.split(": ")[0][len("Game "):]
    line = line.split(": ")[1]
    games = line.split("; ")
    mins = None
    possible = True

    for game in games:
        if not check_possible(game):
            possible = False
        mins = get_minimums(game, mins)
    
    solution1 += int(game_id) if possible else 0
    solution2 += get_product(mins)
    
    
print(solution1)
print(solution2)
