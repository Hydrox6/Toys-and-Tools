import ctypes,random,time

o = False
while True:
  time.sleep(random.randint(2,30))
  if o:
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door closed", None, 0, None)
  else:
    ctypes.windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
  o = not o
