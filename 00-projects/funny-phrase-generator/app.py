# Funny phrase generator
import random

subjects = ["The cat", "A scientist", "The president", "An alien", "A robot"]
verbs = ["jumps over", "analyzes", "discovers", "builds", "destroys"]
objects = ["a fence", "the data", "a new planet", "a machine", "the world"]


def generate_random_phrase():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    return f"{subject} {verb} {obj}."


def execute():
    good_byes = [
        "Goodbye!",
        "See you later!",
        "Take care!",
        "Farewell!",
        "Catch you later!",
    ]
    while True:
        phrase = generate_random_phrase()
        print(phrase)
        user_input = input("Generate another phrase? (y/n): ").strip().lower()
        if user_input != "y":
            # funny and fake emotional goodbye like I'm sad to see you go lol
            print(f"Aw, I'm sad to see you go! {random.choice(good_byes)}")
            break


execute()
