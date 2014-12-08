from Tkinter import *

root = Tk()
root.overrideredirect(1)
root.geometry("%sx%s+-2+-2" % (root.winfo_screenwidth()+4, root.winfo_screenheight()+4))
root.attributes("-topmost", 1)
root.config(background='black',cursor="none")

f = Canvas(root,bg="black")
f.pack(fill="both",expand=1,ipadx=0,ipady=0)

root.mainloop()

##
##YOU MUST F4 OUT OF THIS WINDOW
##
