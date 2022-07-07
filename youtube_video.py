from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube


def select_path():
    path = filedialog.askdirectory()
    # path_label.config(text = path)
    
def download_file():
    get_link = link_field.get()
    # user_path = path_label.cget("text")
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    
    
    
screen = Tk()
title = screen.title("Youtube Downloader")
canvas = Canvas(screen, width = 500, height = 500)
canvas.pack()

logo_img = PhotoImage(file = '/home/mphs/Downloads/youtube_PNG102356.png')
logo_img = logo_img.subsample(4,4)
canvas.create_image(250, 80, image = logo_img)

link_field = Entry(screen, width = 50)
canvas.create_window(250, 220, window = link_field)

link_label = Label(screen, text = "Enter Download Link:")
canvas.create_window(250, 170, window = link_label)


select_btn = Button(screen, text = "Select Path", command = select_path)
canvas.create_window(250, 280, window = select_btn)

download_btn = Button(screen, text = "Download File",command = download_file)

canvas.create_window(250,300, window = download_btn)


screen.mainloop()