import os, time
import math as maths


class File:

    def __init__(self,path,mtime):
        self.path = path
        self.mtime = mtime

class Bind:

    def __init__(self,pathA,pathB,master):
        self.pathA = pathA
        self.pathB = pathB
        self.master = master

    def check(self):
        files = []
        dirs = []

        if self.master == "A":
            master = pathA
            slave = pathB
        elif self.master == "B":
            master = pathB
            slave = pathA

        for d,_,f in os.walk(master):
            d = d.replace("\\","/")
            dirs.append(d[len(master):])
            for x in f:
                print x
                df = d+"/"+x
                rf = df[len(master):]
                mt = int(maths.floor(os.path.getmtime(df)))
                files.append(File(rf,mt))
                
        filedict = dict((x.path,x.mtime) for x in files)
        filenames = [x.path for x in files]

        M2S = []
        deletef = []
        deleted = []
        All = []

        for d,_,f in os.walk(slave):
            d = d.replace("\\","/")
            if not d[len(slave):] in dirs:
                deleted.append(d)
                dead = True
            for x in f:
                print x
                df = d+"/"+x
                rf = df[len(slave):]
                mt = int(maths.floor(os.path.getmtime(df)))
                if not rf in filenames or dead:
                    deletef.append(df)
                else:
                    if mt < filedict[rf]:
                        M2S.append(rf)
                    All.append(rf)

        for x in filenames:
            if not x in All:
                M2S.append(x)

        for x in deletef:
            os.remove(x)
        for x in deleted:
            os.rmdir(x)

        for x in range(0,len(M2S)):
            f = A2B[x]
            fl = open(master+f,"rb")
            c = fl.read()
            fl.close()
            fl = open(slave+f,"wb")
            fl.write(c)
            fl.close()
            t = int(maths.floor(time.time()))
            os.utime(master+f,(t,t))
            os.utime(slave+f,(t,t))

        self.report(M2S)

    def report(self,c):
        t = time.localtime()
        t = "["+str(t[3])+":"+str(t[4])+":"+str(t[5])+"]"
        if len(c) == 0:
            print t+" No Difference"
        else:
            print t+" M>S: "+", ".join(c)


if not os.path.exists(os.getcwd()+"/binds.txt"):
    open("binds.txt","w").close()

with open("binds.txt","r") as fl:r = fl.read()
r = r.split("\n")

binds = []

for x in r:
    if not x == "":
        b = x.split(" || ")
        binds.append(Bind(b[0].replace("\\","/"),b[1].replace("\\","/"),b[2]))


while True:
    for b in binds:
        b.check()
    time.sleep(20)
