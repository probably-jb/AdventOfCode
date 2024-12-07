import numpy as np

def main():
    targets = []
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            items = list(map(int, line.replace('\n', '').replace(':', '').split()))
            targets.append((items[0], items[1:]))

    count = 0
    for target, arr in targets:
        bulk_calc = [arr[0]]

        for i in arr[1:]:
            adds = [val + i for val in bulk_calc]
            mult = [val * i for val in bulk_calc]
            bulk_calc = np.concatenate((adds, mult))

        if target in bulk_calc:
            count += target

    print(count)

main()

