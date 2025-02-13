import pytubefix as yt
import pytubefix.exceptions as errors
import tkinter as tk
from tkinter import messagebox

def Download(link):
    youtubeObject = 0
    try:
        youtubeObject = yt.YouTube(link)
        youtubeObject = youtubeObject.streams.get_audio_only()
    except errors.AgeRestrictedError:
        return 401, "Could not access video" #Unauthorised
    except errors.MembersOnly:
        return 401, "Could not access video" #Unauthorised
    except:
        return 404, "Could not find video" #Video not found
    youtubeObject.download(output_path='Downloads')
    try:
        pass
    except:
        return 422, "Could not download video" #Uprocessable Content
    return 200


def onButtonPress(link):
    responseCode = Download(link)
    if responseCode == 200:
        tk.messagebox.showinfo(title="Succes", message="Download is completed successfully")
    else:
        tk.messagebox.showerror(title="Failed", message=f"Response code: {responseCode[0]}\n{responseCode[1]} ")
        
root = tk.Tk()
root.geometry('400x250')
root.title("Youtube Downloader")

textWindow = tk.Label(root, text="Insert yt link")
textWindow.pack()

linkInput = tk.Entry(root, relief=tk.SUNKEN, width=50)
linkInput.pack()

confirmButton = tk.Button(root, text="Download", command = lambda: onButtonPress(linkInput.get()))
confirmButton.pack()
root.bind('<Return>', lambda x: onButtonPress(linkInput.get())) #x holds the event variable

root.mainloop()