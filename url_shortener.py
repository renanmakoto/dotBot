import pyshorteners
def shorten_url():
    url = input("Enter the URL to shorten: ")
    short_url = pyshorteners.Shortener().tinyurl.short(url)
    print(f"Shortened URL: {short_url}")
