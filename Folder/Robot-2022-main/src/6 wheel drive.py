"""
    This is a demo program showing the use of the DifferentialDrive class,
    specifically it contains the code necessary to operate a robot with
    a single joystick
"""

import wpilib
import wpilib.drive


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        """Robot initialization function"""

        # create motor controller objects
<<<<<<<< Updated upstream:Folder/Robot-2022-main/src/6 wheel_drive.txt
        m_Left = wpilib.Talon(0,1)
        m_Right = wpilib.Talon(2,3)
========
        m_left = wpilib.Talon(0)
        m_right = wpilib.Talon(1)
        #m_rightGroup = wpilib.Talon(2,3)
        #m_leftGroup = wpilib.Talon(0,1)
>>>>>>>> Stashed changes:Folder/Robot-2022-main/src/6 wheel drive.py
        # object that handles basic drive operations
        self.myRobot = wpilib.drive.DifferentialDrive(m_Left,m_Right)
        self.myRobot.setExpiration(0.1)

        # joystick #0
        self.stick = wpilib.Joystick(0)

    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        self.myRobot.arcadeDrive(
            self.stick.getRawAxis(0, 1), self.stick.getRawAxis(1, 2), True
        )


if __name__ == "__main__":
    wpilib.run(MyRobot)
