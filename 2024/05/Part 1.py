def process_lines(file):
    rules = []
    pages = []
    is_rules = True
    for line in file.readlines():
        line = line.replace('\n', '')
        if line == '':
            is_rules = False
            continue

        if is_rules:
            rules.append(list(map(int, line.split('|'))))
        else:
            pages.append(list(map(int, line.split(','))))

    return rules, pages


def check_rules(rules, page):
    for idx, item in enumerate(page):
        disallowed_pages = [rule[0] for rule in rules if rule[1] == item]
        remaining_items = page[idx + 1:]
        if bool(set(disallowed_pages) & set(remaining_items)):
            return 0
    return page[len(page) // 2]


with open('input.txt', 'r') as file:
    rules, pages = process_lines(file)

total = 0
for page in pages:
    total += check_rules(rules, page)

print(total)

