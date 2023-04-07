from tkinter import filedialog
from classes import *
from functions import *

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
    match selectedVariable.get():
        case "OpenJourney t2i":
            t2iFrame.grid(column=0, row=2, sticky="nsew")

        case "OpenJourney i2i":
            i2iFrame.grid(column=0, row=2, sticky="nsew")
        
        case _: # Default
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

t2iEntry = tk.Entry(t2iFrame)
t2iEntry.grid(column=1, row=0, sticky="nsew")

generatet2iBtn = tk.Button(t2iFrame, text="Generate text to image!")
generatet2iBtn.grid(column=0, row=1, columnspan=2, sticky="nsew")


i2iFrame = tk.Frame(root)
i2iLabel = tk.Label(i2iFrame, text="Image to image:")
i2iLabel.grid(column=0, row=0)

frames = [t2iFrame, i2iFrame]

# i2i = tk.Label(root, text="Image to image:")



root.mainloop()