from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.geometry("850x850")    
root.title("Image Slideshow")
# List of image paths
images_path = [
 r"C:\Users\Mangesh\OneDrive\Pictures\1.jpg",
 r"C:\Users\Mangesh\OneDrive\Pictures\3.jpg",
 r"C:\Users\Mangesh\OneDrive\Pictures\5.jpg",
 r"C:\Users\Mangesh\OneDrive\Pictures\6.jpg"   
]

running = False
delay  = 1000
#Resize the images t
# o 1080*1080
image_size=(800,650)
images=[Image.open(path).resize(image_size)for path in images_path]
photo_images=[ImageTk.PhotoImage(image)for image in images]

label = tk.Label(root)
label.pack()

counter_label = tk.Label(root, text="Images")
counter_label.pack()

current_index = 0

def update_image():
    global current_index 
    if running:
     label.config(image=photo_images[current_index])
     
     counter_label.config(text=f"Image {current_index+1} of {len(photo_images)}")  
    
     current_index = (current_index + 1) % len(photo_images)
     root.after(delay,update_image)

slideshow = cycle(photo_images)

def start_slideshow():
    global running
    running = True
    update_image()

def pause_slideshow():
    global running
    running = False

def next_image():
    global current_index
    current_index = (current_index + 1) % len(photo_images)
    label.config(image=photo_images[current_index])

def prev_image():
    global current_index
    current_index = (current_index - 1) % len(photo_images)
    label.config(image=photo_images[current_index])

def set_speed(ms):
    global delay
    delay = ms

button_frame = tk.Frame(root)
button_frame.pack(side="bottom",pady=10)

slow_btn = tk.Button(button_frame, text="Slow", command=lambda: set_speed(2000))
slow_btn.pack(side="left", padx=5)
fast_btn = tk.Button(button_frame, text="Fast", command=lambda: set_speed(500))
fast_btn.pack(side="left", padx=5)

play_button = tk.Button(button_frame, text="Start Slideshow", command=start_slideshow)
play_button.pack(side="left", padx=5)   

pause_button = tk.Button(button_frame, text="pause", command=pause_slideshow)
pause_button.pack(side="left", padx=5)

next_btn = tk.Button(button_frame, text="Next", command=next_image)
next_btn.pack(side="left", padx=5)

prev_btn = tk.Button(button_frame, text="Previous", command=prev_image)
prev_btn.pack(side="left", padx=5)

root.mainloop()
