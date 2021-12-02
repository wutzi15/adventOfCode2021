#part 1
x = 0
y = 0

with open('input.txt', 'r') as f:
    for line in f:
        vals = line.split()
        #print(f"{vals[0]} +x {vals[1]}")
        if vals[0] == 'up':
            y -= int(vals[1])
        elif vals[0] == 'down':
            y += int(vals[1])
        elif vals[0] == 'forward':
            x += int(vals[1])

print(f"Part1: {x} {y}")
print(f"Part1: {x*y}" )

#part 2
x = 0
y = 0
aim = 0

with open('input.txt', 'r') as f:
    for line in f:
        vals = line.split()
        #print(f"{vals[0]} -> {vals[1]}")
        if vals[0] == 'up':
            aim -= int(vals[1])
        elif vals[0] == 'down':
            aim += int(vals[1])
        elif vals[0] == 'forward':
            x += int(vals[1])
            y += aim * int(vals[1])
        #print(f"x:{x} y:{y} aim:{aim}")

print(f"{x} {y}")
print(x*y)
