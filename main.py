from classes import *

root = tk.Tk()
root.title("AIGUI")

OPTIONS = [
    "Select a model",
    "OpenJourney t2i",
    "OpenJourney i2i"
]

def hideshow(event):
    match selectedVariable.get():
        case "OpenJourney t2i":
            t2i.grid(column=0, row=1, sticky="nw")

        case "OpenJourney i2i":
            i2i.grid(column=0, row=1, sticky="nw")
        
        case _:
            t2i.grid_forget()
            i2i.grid_forget()

selectedVariable = tk.StringVar(root)
selectedVariable.set(OPTIONS[0])

modelList = tk.OptionMenu(root, selectedVariable, *OPTIONS, command=hideshow)
modelList.grid(column=0, row=0)

t2i = tk.Label(root, text="Text to image:")
i2i = tk.Label(root, text="Image to image:")



root.mainloop()