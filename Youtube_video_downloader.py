from pytube import YouTube
from sys import argv
link = "https://www.youtube.com/watch?v=PDhkUk0Q6ik"
yt = YouTube(link)

print("Title: ",yt.title)

print("View: ",yt.views)

downloads = yt.streams.get_highest_resolution()

downloads.download('D:\Programming in Python\editedimg')