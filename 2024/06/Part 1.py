def add_tuples(position, direction):
    return tuple(a + b for a, b in zip(position, direction))


def patrol(grid, starting_position):
    steps = []
    current_position = starting_position
    direction = (-1, 0)
    while True:
        step = current_position
        if step not in steps:
            steps.append(step)

        next_position = add_tuples(current_position, direction)

        if next_position in grid:
            has_obstacle = grid[next_position] == '#'

            if has_obstacle:
                x, y = direction
                direction = (y, -x)
            else:
                current_position = next_position
        else:
            return steps


def main():
    grid = {}
    current_position = {}
    with open('input.txt', 'r') as file:
        for l_idx, line in enumerate(file.readlines()):
            for c_idx, char in enumerate(list(line.replace('\n', ''))):
                pos = (l_idx, c_idx)
                grid[pos] = char
                if char == '^':
                    current_position = pos

    steps = patrol(grid, current_position)
    print(len(steps))


main()
