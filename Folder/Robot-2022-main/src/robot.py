#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

from enum import Enum
import wpilib
import wpilib.drive

# our code imports
import drivetrain
import pneumatics
import autonomous
import winch
import ports
import sixwheeldrive
from vision import cameraLaunch
import ports


#!/usr/bin/env python3
"""
    This is a demo program showing the use of the DifferentialDrive class,
    specifically it contains the code necessary to operate a robot with
    a single joystick
"""


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Robot initialization function"""

        # create motor controller objects
        m_left = wpilib.Talon(0)
        m_right = wpilib.Talon(1)

        m_right.setInverted(True)
        # object that handles basic drive operations
        self.myRobot = wpilib.drive.DifferentialDrive(m_left, m_right)
        self.myRobot.setExpiration(0.1)

        # joystick #0
        self.stick = wpilib.Joystick(0)
        wpilib.CameraServer.launch()

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        self.realY = 0
        self.realX = 0

        if (self.stick.getY()<.2):
            self.realY = 0
        else:
            self.realY = self.stick.getY()
        if (self.stick.getX() < .2):
            self.realX = 0
        else:
            self.realX = self.stick.getX()

        

        
        self.myRobot.arcadeDrive(
            self.stick.getY(), -self.stick.getX(), True
        )


if __name__ == "__main__":
    wpilib.run(MyRobot)
