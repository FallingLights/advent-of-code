from string import ascii_lowercase, ascii_uppercase

rucksacks = []
# Read input.txt file line by line save each line in an array
with open('input.txt', 'r', encoding="utf-8") as f:
    for line in f:
        rucksacks.append(line.strip())

# Debug: Print the array
print(rucksacks)

sum_of_rucksacks = 0
for z in rucksacks:
    # If I forget how to do slicing here is the link:
    # https://stackoverflow.com/questions/509211/understanding-slicing
    # First half of the string is the compartment 1
    first_compartment = z[:len(z) // 2]
    # Second half of the string is the compartment 2
    second_compartment = z[len(z) // 2:]

    intersection_points = set(first_compartment).intersection(set(second_compartment))
    # Debug: Print the intersection point
    # print(intersection_points)

    for x in intersection_points:
        if x in ascii_lowercase:
            # print(ascii_lowercase.index(x))
            sum_of_rucksacks += ascii_lowercase.index(x) + 1
        elif x in ascii_uppercase:
            # print(ascii_uppercase.index(x))
            sum_of_rucksacks += ascii_uppercase.index(x) + 27

print("Part 1:" + str(sum_of_rucksacks))

# Part 2

sum_of_rucksacks = 0
for i in range(0, len(rucksacks), 3):
    common_letters = set(ascii_lowercase).union(set(ascii_uppercase))

    for z in range(i, i + 3):
        common_letters = common_letters.intersection(set(rucksacks[z]))

    for x in common_letters:
        if x in ascii_lowercase:
            # print(x)
            sum_of_rucksacks += ascii_lowercase.index(x) + 1
        elif x in ascii_uppercase:
            # print(x)
            sum_of_rucksacks += ascii_uppercase.index(x) + 27

print("Part 2:" + str(sum_of_rucksacks))


