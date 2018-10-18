from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("HostsEditor")
root.geometry("500x500+300+200")

path = "C:\Windows\System32\drivers\etc\hosts"
file = open(path, "r")
textline = file.readlines()
file.close()

sites = []

i = 21
while True:
    try: sites.append(textline[i])
    except: break
    i += 1

siteEntry = Entry(root, textvariable = StringVar())
siteEntry.pack(side = "top", fill = "both")

frameButtons = Frame(root, bg = "#b5b5b5", height = 50)
frameButtons.pack(side = "top", fill = "both")

frameList = Frame(root, bg = "#999999")
frameList.pack(expand = True, fill = "both")

scrollbar = Scrollbar(frameList)
scrollbar.pack(side=RIGHT, fill=Y)

sitesListbox = Listbox(frameList, yscrollcommand=scrollbar.set)
sitesListbox.pack(expand = True, fill = "both")

scrollbar.config(command=sitesListbox.yview)

for site in sites:
    sitesListbox.insert(END, site)

def Delete(event):
    global textline
    try: sel = sitesListbox.curselection()[0]
    except: return
    sitesListbox.delete(sel)
    file = open(path, "w")
    file.write("".join(textline[:21]))
    file.close()
    file = open(path, "a")
    for i in range(sitesListbox.size()):
        file.write(sitesListbox.get(i))
    file.close()
    file = open(path, "r")
    text = file.read()
    file.close()
    file = open(path, "w")
    file.write(text[:-1])
    file.close()
    Refresh("")
        
def Refresh(event):
    global textline
    file = open(path, "r")
    textline = file.readlines()
    file.close()
    sites.clear()
    i = 21
    while True:
        try: sites.append(textline[i])
        except: break
        i += 1
    sitesListbox.delete(0, END)
    for site in sites:
        sitesListbox.insert(END, site)
    return

def Add(event):
    if siteEntry.get() == "" or any(" " == j for j in siteEntry.get()) or any(siteEntry.get() == k.split(" ")[1] for k in sitesListbox.get(0, END)):
        return
    open(path, "a").write("\n127.0.0.1 " + siteEntry.get())
    siteEntry.delete(0, END)
    Refresh("")

def Comment(event):
    global textline
    try: sel = sitesListbox.curselection()[0]
    except: return
    file = open(path, "w")
    file.write("".join(textline[:21]))
    file.close()
    file = open(path, "a")
    for i in range(sitesListbox.size()):
        file.write(sitesListbox.get(i) if sel != i else ("#" + sitesListbox.get(i) if sitesListbox.get(i)[0] != "#" else sitesListbox.get(i)[1:]))
    file.close()
    Refresh("")

deleteButton = Button(frameButtons, text = "Delete", command = lambda: Delete(""))
deleteButton.place(x = 5, y = 5, width = 60, height = 40)
sitesListbox.bind("<Delete>", Delete)

addButton = Button(frameButtons, text = "Add", command = lambda: Add(""))
addButton.place(x = 135, y = 5, width = 60, height = 40)
siteEntry.bind("<Return>", Add)

commentButton = Button(frameButtons, text = "Comment", command = lambda: Comment(""))
commentButton.place(x = 70, y = 5, width = 60, height = 40)
sitesListbox.bind("<Double-Button-1>", Comment)

root.bind("<F5>", Refresh)

root.mainloop()