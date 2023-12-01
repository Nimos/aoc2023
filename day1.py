from aoc import AocData
import re

number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def to_number(word):
    if word in number_words:
        return number_words.index(word) + 1
    return int(word)

def extract_number(inp, part2=False):
    words = "|".join(number_words)
    words_reverse = "|".join([word[::-1] for word in number_words])
    if part2:
        expression = f"([0-9]|{words})"
        expression_reverse = f"([0-9]|{words_reverse})"
    else:
        expression = expression_reverse = "[0-9]"
    match_first = re.search(expression, inp).group()
    match_last = re.search(expression_reverse, inp[::-1]).group()[::-1]

    result = 10*to_number(match_first) + to_number(match_last)
    return result

data = AocData(1)

print(sum([extract_number(line) for line in data.lines()]))
print(sum([extract_number(line, part2=True) for line in data.lines()]))
