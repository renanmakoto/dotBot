import os
import platform
def shutdown_or_restart():
    command = input("\nEnter 'r' to restart or 's' to shutdown: ").lower()
    if command == "r":
        os.system("\nshutdown -r now" if platform.system() != "Windows" else "shutdown -t 0 -r -f")
    elif command == "s":
        os.system("\nshutdown -h now" if platform.system() != "Windows" else "shutdown -s")
    else:
        print("\nInvalid input. Please enter 'r' for restart or 's' for shutdown.")
