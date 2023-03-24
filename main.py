import pytube

# ask user for the video URL

url = input("Enter the YouTube video URL: ")

# create a YouTube object

yt = pytube.YouTube(url)

# get the video stream with the highest resolution

video = yt.streams.get_highest_resolution()

# ask user for the file name to save the video

file_name = input("Enter the file name to save the video (include the extension): ")

title = yt.title

description = yt.description

views = yt.views

length = yt.length

rating = yt.rating

author = yt.author

# Print the video information

print("------------------------------------------------------------")

print("Title:", title)

print("------------------------------------------------------------")

print("Description:", description)

print("------------------------------------------------------------")

print("Views:", views)

print("------------------------------------------------------------")

print("Length:", length, "seconds")

print("------------------------------------------------------------")

print("Rating:", rating)

print("------------------------------------------------------------")

print("Author:", author)

print("------------------------------------------------------------")

# download the video

print("Downloading...")

video.download(filename=file_name)

print("Download completed!")

