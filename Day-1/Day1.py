

# Read txt file line by line, text file contians multiple numbers one number per line,
# numbers belong to multiple users and user are seperated by a blank line

# Create an array to store the numbers of each user
users_sum = []
current_sum = 0

with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        if line.strip():
            # If line is not empty, read number
            current_number = int(line.strip())
            current_sum += current_number
        else:
            # If the line is empty, then the user is finished, so add the sum of the user to the array
            users_sum.append(current_sum)
            current_sum = 0

# Debug: Print the sum of each user
print(users_sum)

# find the index of the user with the highest sum and print the sum
max_index = users_sum.index(max(users_sum))
print("User with highest sum is: " + str(max_index + 1) + " with sum: " + str(users_sum[max_index]))

# find the sum of top 3 users
top_3_sum = sum(sorted(users_sum, reverse=True)[:3])
print("Sum of top 3 users is: " + str(top_3_sum))