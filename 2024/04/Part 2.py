def check_directions(data, line_idx, char_idx):
    if line_idx < 1 or line_idx > len(data)-2 or char_idx < 1 or char_idx > len(data[line_idx])-2:
        return False

    top_left = data[line_idx-1][char_idx-1]
    bottom_right = data[line_idx + 1][char_idx + 1]
    forward_okay = (top_left == 'M' and bottom_right == 'S') or top_left == 'S' and bottom_right == 'M'

    top_right = data[line_idx - 1][char_idx + 1]
    bottom_left = data[line_idx + 1][char_idx - 1]
    backward_okay = (top_right == 'S' and bottom_left == 'M') or top_right == 'M' and bottom_left == 'S'

    return forward_okay and backward_okay


file_path = 'input.txt'
matches = 0
with open(file_path, 'r') as file:
    data = [list(line.strip()) for line in file.readlines()]

for line_idx in range(len(data)):
    for char_idx in range(len(data[line_idx])):
        if data[line_idx][char_idx] == 'A':
            matches += check_directions(data, line_idx, char_idx)

print(matches)
