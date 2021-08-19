from tkinter import *
from tkinter  import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")
    else:
        locationError.config(text="Please Choose A Folder!!",fg="red")

def DownLoadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if (len(url)>1):
      ytdError.config(text="")
      yt = YouTube(url)

      if (choice == choices[0]):
          select = yt.streams.filter(progressive = True).first()
      
      elif(choice == choices[1]):
          select = yt.streams.filter(progressive = True).last()
    
      elif(choice == choices[2]):
          select = yt.streams.filter(only_audio = True).first()

      else:
          ytdError.config(text="Paste Link again!!!",fg="red")


    select.download(Folder_Name)
    ytdError.config(text="Download Completed")     
     
    


root = Tk()
root.title("YOUTUBE VIDEO DOWNLOADER")
root.geometry("450x350")
root.columnconfigure(0,weight=1)


ytLabel = Label(root,text="Enter the URL ofthe Video",font=("Times New Roman",20))
ytLabel.grid()

ytEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytEntryVar)
ytdEntry.grid()


ytdError = Label(root,text="Error Msg",fg="red",font=("Times New Roman",15))
ytdError.grid()

saveLabel = Label(root,text="Save the Video File",font=("Times New Roman",20,"bold"))
saveLabel.grid()

saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

locationError = Label(root,text="Error Msg of Path", fg="red",font=("Times New Roman",15))
locationError.grid()

ytdQuality = Label(root,text="Select Quality",font=("Times New Roman",20))
ytdQuality.grid()

choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownLoadVideo)
downloadbtn.grid()

developerLabel = Label(root,text="Spidy Downloader",font=("Times New Roman",20))
developerLabel.grid()

root.mainloop()