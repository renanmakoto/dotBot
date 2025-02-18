from pytube import YouTube


def download_youtube():
    link = input("Enter the YouTube video URL: ")
    path = input("Enter the directory where you want to save the video: ")

    try:
        yt = YouTube(link)
        yt.streams.get_highest_resolution().download(path)
        print("Download complete! Video saved successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
