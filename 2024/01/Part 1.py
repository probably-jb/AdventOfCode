file_path = 'input.txt'

left_group = []
right_group = []
total = 0
with open(file_path, 'r') as file:
    for line in file:
        cols = line.split('   ')
        left_group.append(int(cols[0]))
        right_group.append(int(cols[1]))

left_group.sort()
right_group.sort()

for i in range(len(left_group)):
    total += abs(left_group[i] - right_group[i])

print(total)
