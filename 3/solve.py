import re

with open('in.txt', 'r') as inp:
    mem = inp.read()

def solve(string):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    mul = re.findall(pattern, string)

    sum = 0

    for inst in mul:
        inst = inst[3:]
        x, y =(inst.strip("()").split(","))
        sum += int(x)*int(y)
    
    return sum

part_one = solve(mem)
print(part_one)

pattern = r"don't\(\)[\s\S]*?(do\(\)|$)"
clean = re.sub(pattern, '', mem)

part_two = solve(clean)
print(part_two)
