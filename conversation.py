import os
import sys
from time import sleep
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import print_separator
def conversation():
    print_separator()
    print("Hello! I'm your chatbot assistant. Let's have a conversation!")
    sleep(1)
    name = input("What's your name? ").strip().capitalize()
    print(f"Nice to meet you, {name}!")
    sleep(1)

    age = input(f"How old are you, {name}? ")
    sleep(1)
    print("That's a great age!")
    sleep(1)

    hobby = input("What do you enjoy doing in your free time? ")
    print(f"That sounds like a lot of fun, {name}!")
    sleep(1)

    job = input("What do you do for a living? ")
    print("That sounds interesting!")
    sleep(1)

    travel = input("If you could travel anywhere in the world, where would you go? ")
    print(f"Wow! {travel} sounds like a fantastic destination.")
    sleep(1)

    favorite_food = input("What is your favorite food? ")
    print(f"Yum! {favorite_food} is delicious!")
    sleep(1)

    favorite_movie = input("Do you have a favorite movie? ")
    if favorite_movie.lower() in ["no", "not really", "none"]:
        print("That's alright! Not everyone has a favorite movie.")
    else:
        print(f"Great choice! {favorite_movie} is a fantastic movie.")
    sleep(1)

    pet = input("Do you have any pets? ")
    if pet.lower() in ["yes", "i do", "of course"]:
        print("That's awesome! Pets are great companions.")
    else:
        print("No worries! Pets are great, but not for everyone.")
    sleep(1)

    weather = input("Do you prefer summer or winter? ")
    print(f"Interesting! {weather.capitalize()} has its own charm.")
    sleep(1)

    print("It's been great talking to you! Let's chat again soon.")
    sleep(1)
