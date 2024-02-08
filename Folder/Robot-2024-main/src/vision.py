#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on

    "Yes!" ~ Gabe
"""

import wpilib



def cameraLaunch():
    
    wpilib.CameraServer.launch()

#from cscore import CameraServer

#def main():
    #cs = CameraServer.getInstance()
    #cs.enableLogging()

    #usb1 = cs.startAutomaticCapture(dev=0)
    #usb2 = cs.startAutomaticCapture(dev=1)

    #cs.waitForever()
