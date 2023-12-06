import re

input = open("input", "r").read().split("\n")

time = re.findall(r"\d+", input[0])
distance = re.findall(r"\d+", input[1])

time2 = int("".join(time))
distance2 = int("".join(distance))

combinded = list(zip(map(int, time), map(int, distance)))

def calculate_distance(chargetime, time):
    return chargetime * (time - chargetime)

def test_calculate_distance():
    input = [(0, 0), (1, 6), (2, 10), (3, 12), (4, 12), (5, 10), (6, 6), (7, 0)]
    for i in input:
        assert calculate_distance(i[0], 7) == i[1]

product = 1
for time, distance in combinded:
    sum = 0
    for i in range(0, time-1):
        calcdistance = calculate_distance(i, time)
        if calcdistance > distance:
            sum += 1
    product *= sum

print("Product: " + str(product))

sum = 0
for i in range(0, time2-1):
    calcdistance = calculate_distance(i, time2)
    if calcdistance > distance2:
        sum += 1


print("Sum: " + str(sum))
