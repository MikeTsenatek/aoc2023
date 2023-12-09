import re
from math import lcm

f = open("input", "r").read().split("\n\n")
start = 'AAA'
end = 'ZZZ'

paths = f[0]
directions = {}
for direction in f[1].split("\n"):
    direction = direction.split(" = ")
    directions[direction[0]] = tuple(re.findall(r"\w+", direction[1]))
    
print(paths)
print(directions)

pathlen = len(paths)
# count = 0

# act = start
# while True:
#     left = directions.get(act)[0]
#     right = directions.get(act)[1]
#     decision = paths[count % pathlen]
#     act = left if decision == 'L' else right
#     count += 1
#     if act == end:
#         break

# print(count)


startpoints = []
for direction in directions:
    if direction.endswith("A"):
        startpoints.append(direction)
        
count = 0     


listofdirections = []
for i in startpoints:
    act = i
    count = 0
    while True:
        left = directions.get(act)[0]
        right = directions.get(act)[1]
        decision = paths[count % pathlen]
        act = left if decision == 'L' else right
        count += 1
        if act.endswith("Z"):
            listofdirections.append(count)
            break
    
print(lcm(*listofdirections))
