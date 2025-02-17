import os
import socket
import platform
import pyqrcode
import pyshorteners
import PyPDF2
from time import sleep
from gtts import gTTS
from pytube import YouTube
import phonenumbers
from phonenumbers import geocoder, carrier
import ip_searcher
import phone_number_company
import qrCodeGenerator1
import shutdownAndRestart
import txtToAudio
import url_shortener
import youtube_downloader
import pdf_converter


def print_separator():
    print("=" * 94)


def ask_choice():
    print("\nWelcome! What would you like to do?")
    options = [
        "Have a conversation",
        "Find a website's IP address",
        "Get phone number information",
        "Generate a QR Code",
        "Shutdown or Restart the computer",
        "Convert text to speech",
        "Shorten a URL",
        "Download a YouTube video",
        "Merge PDFs",
        "Exit"
    ]
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input("Enter your choice (1-10): ")
    return choice


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


def main():
    while True:
        choice = ask_choice()
        if choice == "1":
            conversation()
        elif choice == "2":
            ip_searcher.find_ip()
        elif choice == "3":
            phone_number_company.phone_info()
        elif choice == "4":
            qrCodeGenerator1.generate_qr()
        elif choice == "5":
            shutdownAndRestart.shutdown_or_restart()
        elif choice == "6":
            txtToAudio.text_to_speech()
        elif choice == "7":
            url_shortener.shorten_url()
        elif choice == "8":
            youtube_downloader.download_youtube()
        elif choice == "9":
            pdf_converter.merge_pdfs()
        elif choice == "10":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
