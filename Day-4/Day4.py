# Read input.txt file
with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.read()

# Debug: Print the array
# print(data)

# Part 1
fully_contain = 0
for line in data.split("\n"):
    # if line empty break
    # if not line:
    #    break

    a, b = line.split(",")
    a_start, a_end = map(int, a.split("-"))
    b_start, b_end = map(int, b.split("-"))
    # print(a_start, a_end, b_start, b_end)

    # We test if pairs fully contain each other
    if a_start >= b_start and a_end <= b_end:
        # print("Fully contains")
        fully_contain += 1
    elif b_start >= a_start and b_end <= a_end:
        # print("Fully contains")
        fully_contain += 1

print("Part 1: " + str(fully_contain))

# Part 2
overlaps = 0
# We need to find how many pairs overlap even by one digit
for line in data.split("\n"):
    # if line empty break
    # if not line:
    #    break

    a, b = line.split(",")
    a_start, a_end = map(int, a.split("-"))
    b_start, b_end = map(int, b.split("-"))
    # print(a_start, a_end, b_start, b_end)

    # We test if pairs overlap
    if a_start <= b_start <= a_end:
        # print("Overlap")
        overlaps += 1
    elif b_start <= a_start <= b_end:
        # print("Overlap")
        overlaps += 1

print("Part 2: " + str(overlaps))