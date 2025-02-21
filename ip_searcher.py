import socket
from urllib.parse import urlparse
from time import sleep
def find_ip():
    sleep(0.5)
    site = input("\nEnter the website URL or domain name: ").strip()
    parsed_url = urlparse(site)
    domain = parsed_url.netloc if parsed_url.netloc else site
    try:
        ip_addr = socket.gethostbyname(domain)
        sleep(0.5)
        print(f"\nWebsite: {domain}\nIP Address: {ip_addr}")
    except socket.gaierror:
        sleep(0.5)
        print("\nInvalid website. Please enter a valid domain (e.g., google.com).")
