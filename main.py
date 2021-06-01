import art
import game_data
import random
# import replit


a_and_b = ["", ""]


def random_number():
    return random.randint(1, len(game_data.data))

def compare():
    continue_game = True
    game_round = 0
    a_and_b[0] = game_data.data[random_number()]
    a_and_b[1] = game_data.data[random_number()]
    while continue_game:
        print(art.logo)
        if game_round > 0:
            a_and_b[0] = a_and_b[1]
            a_and_b[1] = game_data.data[random_number()]
            print(f"You're right! Current score: {game_round}")
        print(f"Compare A: {a_and_b[0]['name']}, a {a_and_b[0]['description']}, from {a_and_b[0]['country']} ")
        print(art.vs)
        print(f"Against B: {a_and_b[1]['name']}, a {a_and_b[1]['description']}, from {a_and_b[1]['country']} ")
        choose = input("Who has more followers? Type 'A' or 'B': ")
        print(f"{a_and_b[0]['follower_count']}, {a_and_b[1]['follower_count']}")
        if a_and_b[0]['follower_count'] > a_and_b[1]['follower_count'] and choose.lower() == "a":
            print("you win")
            game_round += 1
            # replit.clear()
        elif a_and_b[0]['follower_count'] < a_and_b[1]['follower_count'] and choose.lower() == "a":
            print("you lose")
            return
        elif a_and_b[0]['follower_count'] > a_and_b[1]['follower_count'] and choose.lower() == "b":
            print("you lose")
            return
        elif a_and_b[0]['follower_count'] < a_and_b[1]['follower_count'] and choose.lower() == "b":
            print("you win")
            game_round += 1
            # replit.clear()
        else:
            print("they are equal")
            return




compare()