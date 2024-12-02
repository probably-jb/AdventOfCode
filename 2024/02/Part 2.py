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


def subset_checker(cols):
    for i in range(len(cols)):
        subset = cols[0:i] + cols[i + 1: len(cols)]
        if is_safe_ascending(subset) or is_safe_descending(subset):
            return True
    return False


file_path = 'input.txt'
safe_count = 0
with open(file_path, 'r') as file:
    for line in file:
        cols = list(map(int, line.split(' ')))
        if subset_checker(cols):
            safe_count += 1

print(safe_count)
