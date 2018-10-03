from tkinter import *
from winreg import *
from tkinter import messagebox

root = Tk()
root.title("HostsEditor")
root.geometry("500x500")

sites = [i.strip() for  i in open("C:\Windows\System32\drivers\etc\hosts", "r").readlines() if i[0] != "#" and i != "\n"]
#print(sites)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

sites_listbox = Listbox(yscrollcommand=scrollbar.set)
 
for site in sites:
    sites_listbox.insert(END, site)
 
sites_listbox.pack(side=TOP, fill=BOTH)
scrollbar.config(command=sites_listbox.yview)









root.mainloop()