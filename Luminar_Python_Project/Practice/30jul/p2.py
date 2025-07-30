"""
Question 2: Print Whether File is Audio, Video, or Other

Question:
Print the type of each file as Audio, Video, or Other.

Audio: .mp3, .wav, .aac

Video: .mp4, .avi, .mkv


Example Input:

files = ["song.mp3", "movie.mp4", "trailer.avi", "audio.wav", "readme.txt", "video.mkv", "clip.mp4"]

Expected Output:

song.mp3 - Audio
movie.mp4 - Video
trailer.avi - Video
audio.wav - Audio
readme.txt - Other
video.mkv - Video
clip.mp4 - Video

"""
files = ["song.mp3", "movie.mp4", "trailer.avi", "audio.wav", "readme.txt", "video.mkv", "clip.mp4"]

Audio=['mp3','wav','aac']

Video=['mp4','avi','mkv']
for i in files:
    d=i.split('.')
    if d[1] in Audio:
        print(i,"-Audio")
    elif d[1] in Video:
        print(i,"-Video")
    else:
        print(i,"-Other")

