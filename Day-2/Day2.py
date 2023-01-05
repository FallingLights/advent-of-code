# Input file:
# A = Rock
# B = Paper
# C = Scissors
# X = Rock
# Y = Paper
# Z = Scissors

# Read input file
with open('input.txt', 'r', encoding="utf-8") as f:
    game = []
    for line in f:
        opponent, response = line.strip().split()
        game.append([opponent, response])

print(game)


def selected_shape_score(shape):
    if shape == 'X':  # Rock
        return 1
    elif shape == 'Y':  # Paper
        return 2
    elif shape == 'Z':  # Scissors
        return 3


# Calculate the score of the game
def simulate_round(opponent_shape, response_shape):
    score = 0
    if (opponent_shape == 'A' and response_shape == 'X') or (opponent_shape == 'B' and response_shape == 'Y') or (
            opponent_shape == 'C' and response_shape == 'Z'):
        score = selected_shape_score(response_shape)
        # Draw: 3 points
        return 3 + score
    elif (opponent_shape == 'A' and response_shape == 'Y') or (opponent_shape == 'B' and response_shape == 'Z') or (
            opponent_shape == 'C' and response_shape == 'X'):
        score = selected_shape_score(response_shape)
        # Win: 6 points
        return 6 + score
    else:
        score = selected_shape_score(response_shape)
        # Loss: 0 points
        return 0 + score


def simulate_round_part2(opponent_shape, response_shape):
    score = 0
    if response_shape == 'X':
        # We need to lose in this round
        if opponent_shape == 'A':
            score = selected_shape_score('Z')
        elif opponent_shape == 'B':
            score = selected_shape_score('X')
        else:
            score = selected_shape_score('Y')

        return 0 + score
    elif response_shape == 'Y':
        # We need to end the round in a draw
        if opponent_shape == 'A':
            score = selected_shape_score('X')
        elif opponent_shape == 'B':
            score = selected_shape_score('Y')
        else:
            score = selected_shape_score('Z')

        return 3 + score
    else:
        # Win: choose the shape that would cause us to win against the opponent's shape
        if opponent_shape == 'A':
            score = selected_shape_score('Y')
        elif opponent_shape == 'B':
            score = selected_shape_score('Z')
        else:
            score = selected_shape_score('X')

        return 6 + score


def simulate_game(game):
    score = 0
    for round_of_game in game:
        score += simulate_round_part2(round_of_game[0], round_of_game[1])
    return score


total_score = 0
for opponent, response in game:
    round_score = simulate_round(opponent, response)
    total_score += round_score

print("Part 1 totalscore:"+str(total_score))

print("Part 2 totalscore:"+str(simulate_game(game)))
