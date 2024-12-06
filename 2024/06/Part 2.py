from copy import deepcopy


def add_tuples(position, direction):
    return tuple(a + b for a, b in zip(position, direction))


def patrol(grid, starting_position, start_direction):
    steps = []
    current_position = deepcopy(starting_position)
    current_direction = deepcopy(start_direction)

    while True:
        step = (current_position, current_direction)
        if step in steps:
            return steps, True

        steps.append(step)
        next_position = add_tuples(current_position, current_direction)

        if next_position in grid:
            if grid[next_position] == '#':
                x, y = current_direction
                current_direction = (y, -x)
            else:
                current_position = next_position
        else:
            return steps, False


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

    steps, _ = patrol(grid, current_position, (-1, 0))

    count = 0
    blockers = []
    i = 0
    for step in steps:
        i += 1
        print(f'{i} of {len(steps)}')
        pos, dir = step
        blocker = add_tuples(pos, dir)

        if blocker == current_position or blocker in blockers or blocker not in grid or grid[blocker] == '#':
            continue
        blockers.append(blocker)

        tmp_grid = deepcopy(grid)
        tmp_grid[blocker] = '#'

        for step_pos, step_dir in steps:
            if add_tuples(step_pos, step_dir) == blocker:
                first_pos, first_dir = step_pos, step_dir
                break

        _, loop = patrol(tmp_grid, first_pos, first_dir)
        if loop:
            count += 1

    print(count)

main()
