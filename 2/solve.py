levels = []

with open("in.txt", "r") as inp:
    for line in inp:
        items = line.strip().split(' ')
        items = [int(x) for x in items]
        levels.append(items)

def part_one(level):

    # if not in sorted order
    if level != sorted(level) and level != sorted(level, reverse=True):
        return 0

    # if gap is bigger than 3 or less than 1
    for i in range(len(level) - 1):
        diff = abs(int(level[i + 1]) - int(level[i]))
        if diff > 3 or diff < 1:
            return 0
    return 1

def part_two(level):
    # do part one and if it fails part one, remove each item and see if it passes
    if part_one(level) != 1:
        for i in range(len(level)):
            if part_one(level[:i] + level[i+1:]) == 1: return 1
    else: 
        return 1

    return 0

one = sum(part_one(level) for level in levels)
two = sum(part_two(level) for level in levels)
print(one)
print(two)
