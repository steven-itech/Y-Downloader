import os
import ctypes
import pyttsx3
from pytube import YouTube, Playlist

ctypes.windll.kernel32.SetConsoleTitleW("Y Downloader :")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def tts(message):
    
    engine.say(message)
    engine.runAndWait()

def clean():
    
    os.system("cls")

if __name__ == "__main__":

    while True:
    
        tts("Would you like to download a video or playlist ?")
        option = input("Would you like to download a video or playlist ? : ")
        
        clean()

        if "video" in option:
        
            tts("Please transmit the URL of the video !")
            video_url = input("Please transmit the URL of the video : ")

            clean()
            
            video = YouTube(video_url)
            
            highresvid = video.streams.get_highest_resolution()
            highresvid.download(os.path.join(os.path.dirname(os.path.abspath(__file__))))

        elif "playlist" in option:
            
            tts("Please transmit the playlist URL !")
            playlist_url = input("Please transmit the playlist URL : ")

            clean()

            p = Playlist(playlist_url)

            print(f"Downloading : {p.title}")

            for video in p.videos:
                
                highresvid = video.streams.get_highest_resolution()
                highresvid.download(os.path.join(os.path.dirname(os.path.abspath(__file__))))
