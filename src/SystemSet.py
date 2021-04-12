import sys
import os
from PySide2.QtCore import *
class Settting(QObject):
    # LCD Backlight
    @Slot(int)
    def Lcdlightset(self,val):
        os.system('sudo chown pi:pi /sys/class/backlight/10-0045/brightness')
        values = '%d'%val
        x = 'echo ' + values + ' > /sys/class/backlight/10-0045/brightness'
        os.system(x)

    #Camera
    @Slot()
    def Cameraon(self):
        os.system('sudo sed -i "s/start_x=0/start_x=1/g" /boot/config.txt')
    @Slot()
    def Cameraoff(self):
        os.system('sudo sed -i "s/start_x=1/start_x=0/g" /boot/config.txt')

    #SSH
    @Slot()
    def SSHon(self):
        os.system('sudo ln -s /lib/systemd/system/ssh.service /etc/systemd/system/multi-user.target.wants/ssh.service')
    @Slot()
    def SSHoff(self):
        os.system('sudo rm /etc/systemd/system/multi-user.target.wants/ssh.service')

    #VNC
    @Slot()
    def VNCon(self):
        os.system('sudo ln -s /usr/lib/systemd/system/vncserver-x11-serviced.service /etc/systemd/system/multi-user.target.wants/vncserver-x11-serviced.service')
    @Slot()
    def VNCoff(self):
        os.system('sudo rm /etc/systemd/system/multi-user.target.wants/vncserver-x11-serviced.service')
        


    #SPI
    @Slot()
    def SPIon(self):
        os.system('sudo sed -i "s/dtparam=spi=off/dtparam=spi=on/g" /boot/config.txt')
    @Slot()
    def SPIoff(self):
        os.system('sudo sed -i "s/dtparam=spi=on/dtparam=spi=off/g" /boot/config.txt')

    #I2C
    @Slot()
    def I2Con(self):
        os.system('sudo sed -i "s/dtparam=i2c_arm=off/dtparam=i2c_arm=on/g" /boot/config.txt')
    @Slot()
    def I2Coff(self):
        os.system('sudo sed -i "s/dtparam=i2c_arm=on/dtparam=i2c_arm=off/g" /boot/config.txt')
    
    #Serial
    @Slot()
    def Serialon(self):
        os.system('sudo sed -i "s/enable_uart=0/enable_uart=1/g" /boot/config.txt')
    @Slot()
    def Serialoff(self):
        os.system('sudo sed -i "s/enable_uart=1/enable_uart=0/g" /boot/config.txt')

    #Shutdown
    @Slot()
    def Shutdown(self):
        os.system('sudo shutdown now')

    #Reboot
    @Slot()
    def Rebooton(self):
        os.system('sudo reboot')

    #Logout
    @Slot()
    def Logout(self):
        sys.exit()
