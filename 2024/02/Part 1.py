def is_safe_ascending(items):
    for i in range(len(items) - 1):
        if items != sorted(items):
            return False
        distance = abs(items[i] - items[i + 1])
        if distance < 1 or distance > 3:
            return False
    return True


def is_safe_descending(items):
    for i in range(len(items) - 1):
        if items != sorted(items, reverse=True):
            return False
        distance = abs(items[i] - items[i + 1])
        if distance < 1 or distance > 3:
            return False
    return True


file_path = 'input.txt'
safe_count = 0
with open(file_path, 'r') as file:
    for line in file:
        cols = list(map(int, line.split(' ')))

        if is_safe_ascending(cols) or is_safe_descending(cols):
            safe_count += 1

print(safe_count)
