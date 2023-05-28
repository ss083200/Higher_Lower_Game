import os
from art import logo, vs
from game_data import data
import random

def clear():
    os.system('cls')

def compare_followers(A, B):
    if A["follower_count"] > B["follower_count"]:
        return "A"
    else:
        return "B"

def play_game():
    clear()
    print(logo)
    A = random.choice(data)
    B = random.choice(data)
    current_score = 0
    should_continue = True

    while should_continue:
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
        print(vs)
        while A == B:
            B = random.choice(data)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

        ans = compare_followers(A, B)
        user_input = input("Who has more followers? 'A' or 'B': ").upper()

        clear()
        print(logo)
        if user_input == ans:
            current_score += 1
            A = B
            print(f"You're right! Current score: {current_score}.")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {current_score}")

play_game()

