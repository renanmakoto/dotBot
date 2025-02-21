from time import sleep
import conversation
import ip_searcher
import phone_number_company
import qr_terminal_saver
import shutdown_and_restart
import txt_to_audio
import url_shortener
import youtube_downloader
import pdf_converter

def print_separator():
    print("=" * 94)

def ask_choice():
    print("\nWelcome! What would you like to do?")
    sleep(0.5)
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

def main():
    while True:
        choice = ask_choice()
        if choice == "1":
            conversation.conversation()
        elif choice == "2":
            ip_searcher.find_ip()
        elif choice == "3":
            phone_number_company.phone_info()
        elif choice == "4":
            qr_terminal_saver.generate_qr()
        elif choice == "5":
            shutdown_and_restart.shutdown_or_restart()
        elif choice == "6":
            txt_to_audio.text_to_speech()
        elif choice == "7":
            url_shortener.shorten_url()
        elif choice == "8":
            youtube_downloader.download_youtube()
        elif choice == "9":
            pdf_converter.merge_pdfs()
        elif choice == "10":
            sleep(0.5)
            print("Goodbye!")
            break
        else:
            sleep(0.5)
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
