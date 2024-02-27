"""
    This is a demo program showing the use of the DifferentialDrive class,
    specifically it contains the code necessary to operate a robot with
    a single joystick
"""

import wpilib
import wpilib.drive
import wpilib.interfaces 
from enum import Enum, auto

class DeadzoneMode(Enum):

    CUTOFF = auto()

    SCALE = auto()


class SixWheelDrivetrain:
    deadzone: float = 0
    deadzone_twist: float = 0
    deadzone_mode: DeadzoneMode = DeadzoneMode.CUTOFF
    speedMultiplier: float = 1
    twistMultiplier: float = 1


    def __init__(self, leftFront: wpilib.interfaces.MotorController, leftBack: wpilib.interfaces.MotorController, rightFront: wpilib.interfaces.MotorController, rightBack: wpilib.interfaces.MotorController):
        """Robot initialization function"""

        # create motor controller objects
        self.leftFront = leftFront
        self.leftBack = leftBack
        self.leftMotorGroup = wpilib.MotorControllerGroup(self.leftFront,self.leftBack)
        self.rightFront = rightFront
        self.rightBack = rightBack
        self.rightMotorGroup = wpilib.MotorControllerGroup(self.rightFront, self.rightBack)
        

        # object that handles basic drive operations
        #self.myRobot = wpilib.drive.DifferentialDrive(self.leftMotorGroup, self.rightMotorGroup)
        #self.myRobot.setExpiration(0.1)

        # joystick #0
        self.stick = wpilib.Joystick(0)

    def constrainJoystick(self, Joystick: wpilib.Joystick):
        mag = Joystick.getMagnitude()
        angle = Joystick.getDirectionDegrees()
        rotate = Joystick.getTwist()

        if mag < self.deadzone:
            mag = 0
        if abs(rotate) < self.deadzone_twist:
            rotate = 0
        mag *= self.speedMultiplier
        rotate *= self.twistMultiplier 
        return [mag, angle, rotate]
    
    def setDeadzone(self, deadzone_move: float, deadzone_twist: float, deadzone_mode: DeadzoneMode = DeadzoneMode.CUTOFF):
        self.deadzone = deadzone_move
        self.deadzone = deadzone_twist
        self.deadzone_mode = deadzone_mode


    def drive(self, Joystick: wpilib.Joystick) -> None:
        """Executed at the start of teleop mode"""
        self.moveRobot(*self.constrainJoystick(Joystick))

    def moveRobot(self, speed: float, direction: float, twist: float):

        raise ValueError("THIS SHOULD BE REPLACED!")
    
    def rightInverted(self,isInverted: bool) -> None:
        self.leftFront.setInverted(isInverted)
        self.leftBack.setInverted(isInverted)

    def leftInverted(self, isInverted: bool) -> None:
        self.rightFront.setInverted(isInverted)
        self.rightBack.setInverted(isInverted)

class DifferentialDrive(SixWheelDrivetrain):

    def __init__(self,leftFront: wpilib.interfaces.MotorController, leftBack: wpilib.interfaces.MotorController, rightFront: wpilib.interfaces.MotorController, rightBack: wpilib.interfaces.MotorController):
        super().__init__(leftFront, leftBack, rightFront, rightBack)
        self.DifferentialDrive = wpilib.drive.DifferentialDrive(
            self.leftMotorGroup, self.rightMotorGroup
        )
        """Runs the motors with tank steering"""
    def moveRobot(self, speed: float, direction: float, twist: float):
        self.DifferentialDrive.curvatureDrive(speed, direction, twist)
