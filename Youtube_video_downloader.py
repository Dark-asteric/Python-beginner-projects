from pytube import YouTube
from sys import argv
link = "Your_video_link_is_here"
yt = YouTube(link)

print("Title: ",yt.title)

print("View: ",yt.views)

downloads = yt.streams.get_highest_resolution()

downloads.download('Your_download_folder_is_here')
