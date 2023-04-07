from tkinter import filedialog
from classes import *
from functions import *
from PIL import ImageTk, Image
from typing import List

root = tk.Tk()
root.title("AIGUI")
# root.geometry("500x200")

OPTIONS = [
    "Select a model",
    "OpenJourney t2i",
    "OpenJourney i2i"
]

def hideshow(event):
    for frame in frames:
        frame.grid_forget()

    if selectedVariable.get() == "OpenJourney t2i":
        t2iFrame.grid(column=0, row=2, sticky="nsew")

    elif selectedVariable.get() == "OpenJourney i2i":
        i2iFrame.grid(column=0, row=2, sticky="nsew")

    else: # Default
        pass

selectedVariable = tk.StringVar(root)
selectedVariable.set(OPTIONS[0])

modelList = tk.OptionMenu(root, selectedVariable, *OPTIONS, command=hideshow)
modelList.grid(column=0, row=1, sticky="nsew")
# TODO: Resize widgets on window resize

directory = tk.StringVar(root)
directoryAskTXT = tk.StringVar(root)
directoryAskTXT.set("Set Directory:")
def setDirectory():
    directory.set(filedialog.askdirectory())
    if directory.get():
        directoryAskTXT.set(directory.get())
directoryAsk = tk.Button(root, textvariable=directoryAskTXT, command=setDirectory)
directoryAsk.grid(column=0, row=0, sticky="nsew")

# currDir = tk.Label(root, textvariable=directory)
# currDir.grid(column=1, row=0, sticky="nsew")

t2iFrame = tk.Frame(root)

t2iLabel = tk.Label(t2iFrame, text="Prompt:")
t2iLabel.grid(column=0, row=0, sticky="nsew")

t2iprompt = tk.StringVar(t2iFrame)
t2iEntry = tk.Entry(t2iFrame, textvariable=t2iprompt)
t2iEntry.grid(column=1, row=0, sticky="nsew")

# Tk Images List
saved_tk_images: List[tk.Label] = []

def generatet2i():
    if not (t2iEntry.get()):
        return
    
    for label in saved_tk_images:
        label.destroy()

    print(f"Prompt: {t2iEntry.get()}")
    files = openjourney(t2iEntry.get())

    for imagename, prompt in files.items():
        print(imagename, prompt)
        image = Image.open(imagename)
        image = image.resize((100, 100)) # Resize the image to fit in grid
        image_tk = ImageTk.PhotoImage(image)
        image_tk_list.append(image_tk)

    # Create a grid of images
    for i in range(len(image_tk_list)):
        row = i // 3 # Three images per row
        col = i % 3
        imagesLbl = tk.Label(t2iGeneratedFrame, image=image_tk_list[i])
        imagesLbl.grid(row=row, column=col)
        saved_tk_images.append(imagesLbl)
        
        

generatet2iBtn = tk.Button(t2iFrame, text="Generate text to image!", command=generatet2i)
generatet2iBtn.grid(column=0, row=1, columnspan=2, sticky="nsew")

image_tk_list = []

t2iGeneratedFrame = tk.Frame(t2iFrame)
t2iGeneratedFrame.grid(column=0, row=2)


i2iFrame = tk.Frame(root)
i2iLabel = tk.Label(i2iFrame, text="Image to image:")
i2iLabel.grid(column=0, row=0)

frames = [t2iFrame, i2iFrame]

# i2i = tk.Label(root, text="Image to image:")

def on_closing():
    for label in saved_tk_images:
        label.destroy()

    root.destroy()

# Bind on_closing function to close window
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()