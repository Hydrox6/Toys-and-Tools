import time,winsound,os
from threading import Thread
os.system("title Alarm")
os.system("color 0B")
off = False
def wait():
    global off
    raw_input("PRESS ENTER TO TURN IT OFF")
    off = True
alarm = raw_input("hh:mm >")
alarm = alarm.split(":")
hour = int(alarm[0])
minute = int(alarm[1])
while True:
    t = time.localtime()
    if t.tm_hour == hour:
        if t.tm_min == minute:
            break
    time.sleep(2)
Thread(target=wait,args=()).start()
while not off:winsound.PlaySound("{SOUND}",winsound.SND_FILENAME)#replace {SOUND} with the path to the alarm sound file
