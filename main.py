import pytube as yt
import pytube.exceptions as errors
import tkinter as tk

youtubeObject = 0

def Download(link):
    try:
        youtubeObject = yt.YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
    except errors.AgeRestrictedError:
        return 401, "Could not access video" #Unauthorised
    except errors.MembersOnly:
        return 401, "Could not access video" #Unauthorised
    except:
        return 404, "Could not find video" #Video not found
    try:
        youtubeObject.download()
    except:
        return 422, "Could not download video" #Uprocessable Content
    print("Download is completed successfully")

root = tk.Tk()
root.title="Oi"

root.mainloop()