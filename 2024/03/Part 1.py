import re

file_path = 'input.txt'
total = 0
with open(file_path, 'r') as file:
    line = file.read().replace('\n', '')
    for match in re.findall(r"mul\((\d+),(\d+)\)", line):
        total += int(match[0]) * int(match[1])

print(total)
