import subprocess, os, string
from ctypes import windll

class Shell:

    def __init__(self,typee,width=70,startpath=os.getcwd().replace("\\","/")+"/"):
        self.type = typee
        self.startpath = startpath
        self.width = width
        self.hel = {"help":[self.help,"Displays help\n\n\tUsage: help\n\t       help [command]"],
                    "cd":[self.cd,"Changes directory. Using '..' goes to parent directory\n\n\tUsage: cd [directory]\n\t       cd .."],
                    "exit":[self.exit,"Exits Program\n\n\tUsage: exit"]}

    def setCustom(self,c):
        self.custom = c
    
    def doDrives(self):
        while True:
            drives = []
            bitmask = windll.kernel32.GetLogicalDrives()
            for letter in string.uppercase:
                if bitmask & 1:
                    drives.append(letter)
                bitmask >>= 1
            print "\n\n\n\n"
            print "=" * (self.width+7)
            print "| "+"Computer".ljust(self.width+4)+"|"
            print "=" * (self.width+7)
            for x in range(0,len(drives)):
                print "| "+(drives[x]+":/").ljust(self.width+4)[:self.width+4]+"|"
            print "=" * (self.width+7)
            
            i = raw_input(">").rstrip()
            if self.shell(i,True,[[],drives]) == 1:
                break

    def start(self):
        breaker = ""
        self.running = True
        while self.running:
            if self.type == "custom":
                files = self.custom[2]
                folders = self.custom[1]
                dirname = self.custom[0]
            elif self.type == "filesystem":
                for dirname1,folders1,files1 in os.walk(self.startpath):
                    dirname = dirname1
                    folders = folders1
                    files = files1
                    break

            print breaker
            breaker = "\n\n"
            print "=" * (self.width+7)
            print "| "+dirname.ljust(self.width+4)+"|"
            print "=" * (self.width+7)
            print "| ^ - "+"..".ljust(self.width)+"|"
            for x in range(0,len(folders)):
                print "| D - "+folders[x].ljust(self.width)[:self.width]+"|"
                for y in range(1,(len(folders[x])//self.width)+1):
                        print "|     "+folders[x][self.width*y:(self.width*y)+self.width].ljust(self.width)[:self.width]+"|"
            for x in range(0,len(files)):
                print "| F - "+files[x].ljust(self.width)[:self.width]+"|"
                for y in range(1,(len(files[x])//self.width)+1):
                        print "|     "+files[x][self.width*y:(self.width*y)+self.width].ljust(self.width)[:self.width]+"|"
            print "=" * (self.width+7)

            while True:
                i = raw_input(">").rstrip()
                if not self.shell(i,False,[files,folders]) == 0:
                    break

    def stop(self):
        self.running = False
                
    
    def shell(self,i,root,things):
        files, folders = things
        try:
            return self.hel[i.split(" ")[0]][0](i,files,folders,root)
        except KeyError:
            print "Error: command not found"
            return 0

    def cd(self,i,files,folders,root):
        if not root:
            if i[3:] == "..":
                self.startpath = "/".join(self.startpath.split("/")[0:-2])+"/"
                if self.startpath == "/":
                    self.doDrives()
                    return 1
            elif "/" in i[3:]:
                if os.path.exists(i[3:]):
                    self.startpath = i[3:]
                    return 1
                else:
                    print "Error: path not found"
                    return 0
            else:
                itd = []
                for x in range(0,len(folders)):
                    if folders[x].lower()[0:len(i[3:])] == i[3:].lower():
                        itd.append(folders[x])
                if len(itd) == 1:
                    self.startpath += idt[x]+"/"
                    return 1
                elif len(itd) == 0:
                    print "Error: no .pyc files found"
                    return 0
                else:
                    print "=" * (self.width+7)
                    print "| "+"Select Folder".ljust(self.width+4)+"|"
                    print "=" * (self.width+7)
                    tl = len(str(len(itd)))
                    for x in range(0,len(itd)):
                        print "| "+str(x+1).rjust(tl)+" - "+itd[x].ljust(self.width-(tl-1))[:self.width-(tl-1)]+"|"
                        for y in range(1,(len(itd[x])//self.width)+1):
                                print "| "+(" "*(tl+3))+itd[x][self.width*y:(self.width*y)+self.width].ljust(self.width-(tl-1))[:self.width-(tl-1)]+"|"
                    print "=" * (self.width+7)
                    while True:
                        ii = raw_input(">")
                        try:
                            ii = int(ii)
                            break
                        except:
                            print "Error: input an integer"
                    self.startpath += itd[ii-1]+"/"
                    return 1
        elif root:
            if "/" in i[3:] and i[3:].count("/") > 1:
                if os.path.exists(i[3:]):
                    self.startpath = i[3:]
                    return 1
                else:
                    print "Error: path not found"
                    return 0
            elif not len(i[3:]) > 3:
                if i[3].upper() in folders:
                    self.startpath = i[3]+":/"
                    return 1
                else:
                    print "Error: drive not found"
                    return 0
            else:
                print "Error: drive not found"
                return 0
            
    def exit(self,i,files,folders,root):self.running = False
             
    def help(self,i,files,folders,root):
        if i[0:4] == "help" and len(i) == 4:
            print "\nShell help:\n"
            for k,v1 in self.hel.items():
                v = v1[1].split("\n\n\t")[0]
                print "\n\n"+v1[1].split("Usage: ")[1].replace("\n\t       "," || ")+":"
                for y in range(0,(len(v)//self.width)+1):
                    print v[self.width*y:(self.width*y)+self.width].ljust(self.width)[:self.width]
            print
            raw_input("Press Enter to continue")
            return 1
        elif i[0:5] == "help ":
            print "\nShell Help:\n"
            try:
                t = self.hel[i[5:]][1]
            except KeyError:
                t = "Command not found: "+i[5:]
            print t
            print
            raw_input("Press Enter to continue")
            return 1
        else:
            print "Error: command not found"
            return 0

    def addCommand(self,name,command,helptext):
        if name in self.hel:
            return False
        elif not name in self.hel:
            self.hel[name] = [command,helptext[0]+"\n\n\tUsage: "+("\n\t       ".join([x for x in helptext[1]]))]
            return True

    def remCommand(self,name):
        if name in self.hel:
            del self.hel[name]
            return True
        elif not name in self.hel:
            return False

