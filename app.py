import tkinter as tk
from tkinter import filedialog, Text
import os, subprocess

root = tk.Tk()
root.title('Daily Startup Apps')
apps = []

# split whitespace between saves.
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp(): 
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*"), ("apps", "*.app")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
        
def runApps():
    for app in apps:
        # os.startfile(app) does not work on mac - alternative is using subprocess.call
	    subprocess.call(["/usr/bin/open", "-W", "-n", "-a", app])


canvas = tk.Canvas(root, height= 750, width= 750, bg="#42f5f5")
# allows you to add styling to the gui
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=.8, relheight=.8, relx=.1,rely=.1)

openFile = tk.Button(root, text="Open File", justify= "center", padx=10, pady=5, fg="black", bg="#42f5f5", command=addApp)
openFile.pack(side="left", padx=150)

runMyApps = tk.Button(root, text="Run Apps",justify= "center", padx=10, pady=5, fg="black", bg="#42f5f5", command=runApps)
runMyApps.pack(side="right", padx=150)


# openFile.grid(column=0, row=0)
# runMyApps.grid(column=1, row=0)

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# saving as a txt file

with open('save.txt', 'w') as f: 
    for app in apps:
        f.write(app + ',')