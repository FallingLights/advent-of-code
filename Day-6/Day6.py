def uniqueCharacters(str):
    sorted_string = ''.join(sorted(str))
    for k in range(len(sorted_string) - 1):
        if sorted_string[k] == sorted_string[k + 1]:
            return False

    return True


# Read input.txt file
with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.read()

message = data.rstrip()

# Part 1
# We grab a substring of 4 characters, starting at index 1, we check if all 4 cheracters are unique
# We do this until we reach the end of the string
# We use a set to check if all characters are unique
for i in range(0, len(message), 1):
    substring = message[i:i+4]
    print(substring, uniqueCharacters(substring))
    # Check if string is unique
    if uniqueCharacters(substring):
        print("Part 1: "+str(i+4))
        break

# Part 2
for i in range(0, len(message), 1):
    substring = message[i:i+14]
    # Check if string is unique
    if uniqueCharacters(substring):
        print("Part 2: "+str(i+14))
        break