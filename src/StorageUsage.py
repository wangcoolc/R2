import sys
import os
from PySide2.QtCore import *
class StorageUsage(QThread):
    StoragSignal = Signal(int)
    def __init__(self):
        super().__init__()
    
    def run(self):
        p = os.popen("df -h /")
        i = 0
        while True:
            i = i +1
            line = p.readline()
            if i==2:
                DISK_stats = line.split()[1:5]
                DISK_total = int(str(DISK_stats[0][0:2]))
                DISK_used = int(str(DISK_stats[1][0:2]))

                # print("DISK_total",DISK_total)
                # print("DISK_used",DISK_used)

                val = round(int((DISK_used / DISK_total) * 100),0)
                # print("StorageUsage",val)
                self.StoragSignal.emit(int(val))
                self.sleep(1)
                p = os.popen("df -h /")
                i = 0
