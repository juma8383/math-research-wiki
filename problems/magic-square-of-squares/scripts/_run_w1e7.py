import os, psutil, sys
p = psutil.Process(os.getpid())
p.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)
exec(open(r"C:\Claude-Code\Math\problems\magic-square-of-squares\scripts\mss_d_additive_W1e7.py").read())
