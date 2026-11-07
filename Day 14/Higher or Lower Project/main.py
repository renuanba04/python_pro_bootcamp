from random import choice
import art
from game_data import data

SCORE = 0

def random_celebrity():
    """Returns celebrity details as a dictionary"""
    return choice(data)

def display(a_details, b_details):
    """Displays Celeb A vs Celeb B in a cool fashion"""
    print(f"Compare A: {a_details["name"]}, a {a_details["description"]}, from {a_details["country"]}")
    print(art.vs)
    print(f"Against B: {b_details["name"]}, a {b_details["description"]}, from {b_details["country"]}")

def check_answer(a_details, b_details, guess):
    """Checks whether user's guess is right, updates score and returns the game_over status"""
    global SCORE
    a_followers = a_details["follower_count"]
    b_followers = b_details["follower_count"]

    if guess == 'A' and a_followers > b_followers or \
       guess == 'B' and b_followers > a_followers or \
       a_followers == b_followers:
        SCORE += 1
        return False

    return True

def check_answer_opt2(a_followers, b_followers, guess):
    """Takes user's guess, followers' count and returns whether the guess is right"""
    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"

# game function
def game():
    """Higher or Lower Game for Instagram Followers"""

    a = random_celebrity()
    is_guess_wrong = False
    while not is_guess_wrong:

        print(art.logo)
        if SCORE != 0:
            print(f"You're right! Current score: {SCORE}")

        b = random_celebrity()
        display(a, b)
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        is_guess_wrong = check_answer(a, b, guess)
        print("\n" * 20)
        if is_guess_wrong:
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {SCORE}")
            return
        a = b # for next round Celeb B becomes Celeb A


def game_opt2():
    """Higher or Lower Game for Instagram Followers"""
    global SCORE
    print(art.logo)
    b = random_celebrity()
    should_game_continue = True
    while should_game_continue:

        a = b
        b = random_celebrity()
        display(a, b)
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        is_right = check_answer_opt2(a["follower_count"], b["follower_count"], guess)
        print("\n" * 20)
        print(art.logo)

        if is_right:
            SCORE += 1
            print(f"You're right! Current score: {SCORE}")
        else:
            print(f"Sorry, that's wrong. Final score: {SCORE}")
            should_game_continue = False

# Start game here
game()
# game_opt2()

