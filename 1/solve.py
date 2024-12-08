list_one, list_two = [], []

with open('in.txt', "r") as inp:
    for line in inp:
        items = line.strip().split('   ')
        list_one.append(items[0])
        list_two.append(items[1])

list_one.sort()
list_two.sort()

part_one = sum(abs(int(list_one[i]) - int(list_two[i])) for i in range(len(list_one)))
part_two = sum(int(x) * list_two.count(x) for x in (list_one))
print(f"{part_one}\n{part_two}")