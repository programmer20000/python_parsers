from pytube import YouTube

def download_video():
    DOWNLOAD_FOLDER = fr"D:\python\python_lesson\parsers\parser_video\music_2022/{'music_2022'.upper()}"

    try:
        with open(file="music_2022/link_video_unic.txt", mode="r") as file:
            source = file.read()
            for links in source.split("\n"):
                video_object = YouTube(links)
                stream = video_object.streams.get_highest_resolution()
                stream.download(DOWNLOAD_FOLDER)
                print("Successful")
    except:
        print("Done")

download_video()