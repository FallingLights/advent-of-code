import re

# Read input.txt file
with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.read()

# Split data between initial state and instructions
initial_state, instructions = data.rstrip().split("\n\n")
# print(initial_state.split("\n"))
*towers, indices = initial_state.split("\n")
# print(towers, indices)
tower_count = int(indices.strip().split()[-1])

tower_stacks = [[] for _ in range(tower_count)]

for line in towers[::-1]:

    for i in range(tower_count):
        try:
            tower_char = line[i * 4 + 1]
        except IndexError:
            tower_char = ' '

        if tower_char != " ":
            tower_stacks[i].append(tower_char)

# print(tower_stacks)

tower_stacks_2 = [line.copy() for line in tower_stacks]  # for part 2

# print(tower_stacks_2)

for line in instructions.split("\n"):
    # x = how many crates to move, y = from which tower, z = to which tower
    x, y, z = map(int, re.fullmatch(r"move (\d+) from (\d+) to (\d+)", line).groups())

    for _ in range(x):
        new = tower_stacks[y - 1].pop()
        tower_stacks[z - 1].append(new)

    # Part 2
    tower_stacks_2[z - 1].extend(tower_stacks_2[y - 1][-x:])
    tower_stacks_2[y - 1] = tower_stacks_2[y - 1][:-x]  # Slice is faster than pop()

print(tower_stacks)
print("Part 1: "+''.join(s[-1] for s in tower_stacks))  # We use -1 to get the last element of the list
print("Part 2: "+''.join(s[-1] for s in tower_stacks_2))
