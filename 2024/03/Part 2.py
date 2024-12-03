import re

file_path = 'input.txt'
track = 1
total = 0
with open(file_path, 'r') as file:
    line = file.read().replace('\n', '')
    for match in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line):
        if match == "do()" or match == "don't()":
            track = match == "do()"
        else:
            values = list(map(int, match.replace('mul(', '').replace(')', '').split(',')))
            total += (values[0] * values[1]) * track

print(total)
