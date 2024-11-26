from tkinter import *
from PIL import Image

root = Tk()
file = "sponge.gif"

info = Image.open(file)
frames = info.n_frames
print(frames)

im = [PhotoImage(file = file, format = f"gif -index {i}") for i in range(frames)]

anim = None
count = 0
def animation(count):
	global anim
	im2 = im[count]
	gif_label.configure(image = im2)

	count = 1
	if count == frames:
		count = 0

	root.after(50,lambda: animation(count))

def stop_animation():
	global anim
	root.after_cancel(anim)


gif_label = Label(image = "")
gif_label.pack()

start = Button(text = "start", command =lambda: animation(count))

stop = Button(text = "stop", command = stop_animation)
stop.pack()

