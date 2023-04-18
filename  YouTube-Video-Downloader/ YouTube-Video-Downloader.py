import os
import pytube

# Prompt the user to enter the URL of the YouTube video they want to download
video_url = input("Enter the URL of the YouTube video you want to download: ")

# Create a YouTube object and get the video
yt = pytube.YouTube(video_url)
video = yt.streams.get_highest_resolution()

# Create a "videos" directory if it doesn't exist already
if not os.path.exists("videos"):
    os.makedirs("videos")

# Download the video to the "videos" directory
video.download(output_path="videos")
