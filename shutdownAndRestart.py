import os
import platform
def shutdown_or_restart():
    command = input("Enter 'r' to restart or 's' to shutdown: ").lower()

    if command == "r":
        os.system("shutdown -r now" if platform.system() != "Windows" else "shutdown -t 0 -r -f")
    elif command == "s":
        os.system("shutdown -h now" if platform.system() != "Windows" else "shutdown -s")
    else:
        print("Invalid input. Please enter 'r' for restart or 's' for shutdown.")
