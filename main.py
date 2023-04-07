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

t2iFrame = tk.Frame(root)

t2iLabel_Prompt = tk.Label(t2iFrame, text="Prompt")
t2iLabel_Prompt.grid(column=0, row=0, sticky="nsew")

t2iEntry_Prompt = tk.Entry(t2iFrame, textvariable=tk.StringVar(t2iFrame))
t2iEntry_Prompt.grid(column=0, row=1, sticky="nsew")

t2iLabel_Count = tk.Label(t2iFrame, text="Count")
t2iLabel_Count.grid(column=1, row=0, sticky="nsew")

t2iEntry_Count = tk.Entry(t2iFrame, textvariable=tk.StringVar(t2iFrame))
t2iEntry_Count.grid(column=1, row=1, sticky="nsew")


# Tk Images List
saved_tk_images: List[tk.Label] = []

def generatet2i():
    if not t2iEntry_Prompt.get():
        return
    
    dir = directory.get() if directory.get() else None
    
    
    for label in saved_tk_images:
        label.destroy()

    files = openjourney(
        dir, 
        t2iEntry_Prompt.get(), 
        count=int(t2iEntry_Count.get())
    )

    for imagename, prompt in files.items():
        print(prompt)
        print(f"{imagename}\n")
        image = Image.open(imagename)
        image = image.resize((100, 100)) # Resize the image to fit in grid
        image_tk = ImageTk.PhotoImage(image)
        image_tk_list.append(image_tk)

    imageFrame = tk.Frame(t2iGeneratedFrame)
    # Create a grid of images
    for i in range(len(image_tk_list)):
        row = i // 3 # Three images per row
        col = i % 3
        imagesLbl = tk.Label(imageFrame, image=image_tk_list[i])
        imagesLbl.grid(row=row, column=col)
        saved_tk_images.append(imagesLbl)
        imageFrame.grid(row=0, column=0, columnspan=2)

generatet2iBtn = tk.Button(t2iFrame, text="Generate text to image!", command=generatet2i)
generatet2iBtn.grid(column=0, row=2, columnspan=2, sticky="nsew")

image_tk_list = []

t2iGeneratedFrame = tk.Frame(t2iFrame)
t2iGeneratedFrame.grid(column=0, row=3)


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