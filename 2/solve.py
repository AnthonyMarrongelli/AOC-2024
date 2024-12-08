def process_in(file):
    
    levels = []

    with open(file, 'r') as inp:
        for line in inp:
            items = line.strip().split(' ')
            items = [int(x) for x in items]
            levels.append(items)

    return levels

def safe(level):
    
    faults = 0
    for i in range(len(level)-1):
        if




    for i in range(len(level) - 1):
        diff = abs(int(level[i + 1]) - int(level[i]))
        if diff != 3 and diff != 1 and diff != 2:
            faults += 1
            if faults > 1:
                return 0

    return 1

levels = process_in('test.txt')
part_one = sum(safe(level) for level in levels)
print(part_one)