import socket
def find_ip():
    site = input("Enter the website URL: ")
    try:
        ip_addr = socket.gethostbyname(site)
        print(f"Website: {site}\nIP Address: {ip_addr}")
    except socket.gaierror:
        print("Invalid website URL. Please try again.")
