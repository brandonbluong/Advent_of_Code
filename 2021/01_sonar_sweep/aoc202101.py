MEASUREMENT_INCREASES = 0

with open("advent_day_1.txt") as depth:
    num_depth = [int(line.strip()) for line in depth]

for i in range(len(num_depth) - 1):
    if num_depth[i + 1] > num_depth[i]:
        MEASUREMENT_INCREASES += 1

print(MEASUREMENT_INCREASES)

# Part 2


def window_fn(input):
    WINDOW_INCREASES = 0

    for i in range(len(num_depth) - 1):
        if i + 3 == len(num_depth):
            return WINDOW_INCREASES
        window = num_depth[i] + num_depth[i + 1] + num_depth[i + 2]
        if (window - num_depth[i] + num_depth[i + 3]) > window:
            WINDOW_INCREASES += 1


print(window_fn(num_depth))
