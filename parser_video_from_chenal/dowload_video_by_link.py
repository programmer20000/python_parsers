from pytube import YouTube

def download_video():
    DOWNLOAD_FOLDER = fr"D:\python\python_lesson\parsers\python_parsers\parser_playlist_video\al/{'alyn2'.upper()}"

    try:
        with open(file="al/link_video_unic.txt", mode="r") as file:
            source = file.read()
            for links in source.split("\n"):
                video_object = YouTube(links)
                stream = video_object.streams.get_highest_resolution()
                stream.download(DOWNLOAD_FOLDER)
                print("Successful")
    except:
        print("Done")

download_video()