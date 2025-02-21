from gtts import gTTS
def text_to_speech():
    text = input("Enter the text you want to convert into speech: ")
    tts = gTTS(text=text, lang='en')
    tts.save("audio.mp3")
    print("Audio file has been saved as 'audio.mp3'.")
