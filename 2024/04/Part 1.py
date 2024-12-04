def check_directions(data, line_idx, char_idx, direction, step):
    line_delta, char_delta = direction
    check_value = ['X', 'M', 'A', 'S'][step]
    x_val = line_idx + (line_delta * step)
    y_val = char_idx + (char_delta * step)

    if x_val < 0 or x_val >= len(data) or y_val < 0 or y_val >= len(data[line_idx]):
        return False

    if data[x_val][y_val] != check_value:
        return False

    if step == 3:
        return True

    return check_directions(data, line_idx, char_idx, direction, step + 1)


file_path = 'input.txt'
directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1)]
matches = 0
with open(file_path, 'r') as file:
    data = [list(line.strip()) for line in file.readlines()]

for line_idx in range(len(data)):
    for char_idx in range(len(data[line_idx])):
        if data[line_idx][char_idx] == 'X':
            matches += sum(check_directions(data, line_idx, char_idx, dir, 1) for dir in directions)

print(matches)
