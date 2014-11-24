from Tkinter import *

root = Tk()
root.overrideredirect(1)
root.geometry("%sx%s+0+0" % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.attributes("-topmost", 1)

f = Canvas(root,bg="black")
f.pack(fill="both",expand=1)

root.mainloop()

##
##YOU MUST F4 OUT OF THIS WINDOW
##
