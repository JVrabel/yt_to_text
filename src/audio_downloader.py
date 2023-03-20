import pytube


def audio_down(link):
    data = pytube.YouTube(link)

    # Converting and downloading as 'MP4' file
    audio = data.streams.get_audio_only()
    audio.download()