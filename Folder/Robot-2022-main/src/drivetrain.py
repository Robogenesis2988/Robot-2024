import wpilib
import wpilib.drive
import wpilib.interfaces
from enum import Enum, auto


class DeadzoneMode(Enum):

    CUTOFF = auto()
    """This will cut off any value"""

    SCALE = auto()
    """
    ! Not yet implemented

    This will move the scale from joystick_zero=0 to joystick_limit=1 to deadzone=0 and joystick_limit=1
    """


class DriveTrain:
    deadzone: float = 0
    deadzone_twist: float = 0
    deadzone_mode: DeadzoneMode = DeadzoneMode.CUTOFF
    speedMultiplier: float = 1
    twistMultiplier: float = 1
    

    def __init__(self, leftFront: wpilib.interfaces.MotorController, leftRear: wpilib.interfaces.MotorController, rightFront: wpilib.interfaces.MotorController, rightRear: wpilib.interfaces.MotorController) -> None:
        self.leftFront = leftFront
        self.leftRear = leftRear
        self.rightFront = rightFront
        self.rightRear = rightRear
        self.stick = wpilib.Joystick(0)
        self.realX = 0
        self.realY = 0
        self.realZ = 0

    def constrainJoystick(self, Joystick: wpilib.Joystick):
        """
        Constrains joystick using deadzone & deadzone_twist values & applies speed multiplier

        anything below the deadzone/deadzone_twist value will be cut off(set to 0)
        """
        mag = Joystick.getMagnitude()
        angle = Joystick.getDirectionDegrees()
        rotate = Joystick.getTwist()
        if mag < self.deadzone:  # implement based on self.deadzone_mode
            mag = 0
        if abs(rotate) < self.deadzone_twist:  # absolute value b/c rotate goes from -1 to 1
            rotate = 0

        mag *= self.speedMultiplier
        rotate *= self.twistMultiplier
        return [mag, angle, rotate]

    def setDeadzone(self, deadzone_move: float, deadzone_twist: float, deadzone_mode: DeadzoneMode = DeadzoneMode.CUTOFF):
        self.deadzone = deadzone_move
        self.deadzone_twist = deadzone_twist
        self.deadzone_mode = deadzone_mode

    def drive(self, Joystick: wpilib.Joystick) -> None:
        """
        DO NOT REPLACE!

        override moveRobot instead
        """
        self.moveRobot(*self.constrainJoystick(Joystick))

    def moveRobot(self, speed: float, direction: float, twist: float):
        """
        Drive the robot in a direction at a speed for a duration

        :param speed: the speed of the robot[0, 1]

        :param direction: angle to drive at from [-180, 180]

        Angles are measured clockwise from the positive X axis. The robot's speed is independent from its angle or rotation rate.

        :param twist: the speed of the robot in the z(rotational) axis[-1, 1]
        """
        raise ValueError("THIS SHOULD BE REPLACED!")

    def rightInverted(self, isInverted: bool) -> None:
        self.rightFront.setInverted(isInverted)
        self.rightRear.setInverted(isInverted)

    def leftInverted(self, isInverted: bool) -> None:
        self.leftFront.setInverted(isInverted)
        self.leftRear.setInverted(isInverted)

    def motorTest(self, timer: wpilib.Timer) -> None:
        # Test each motor one by one
        # FR FL RR RL
        duration = 3
        speed = 0.4

        self.rightFront.set(speed)
        if timer.get() > duration*4:
            self.leftRear.stopMotor()
        elif timer.get() > duration*3:
            self.rightRear.stopMotor()
            self.leftRear.set(speed)
        elif timer.get() > duration*2:
            self.leftFront.stopMotor()
            self.rightRear.set(speed)
        elif timer.get() > duration*1:
            self.rightFront.stopMotor()
            self.leftFront.set(speed)




class MecanumDrive(DriveTrain):
    def __init__(self, leftFront: wpilib.interfaces.MotorController, leftRear: wpilib.interfaces.MotorController, rightFront: wpilib.interfaces.MotorController, rightRear: wpilib.interfaces.MotorController) -> None:
        # run the parent's __init__ function
        super().__init__(leftFront, leftRear, rightFront, rightRear)
        self.MecanumDrive = wpilib.drive.MecanumDrive(
            self.leftFront, self.leftRear, self.rightFront, self.rightRear)  # create a mecanum drive object

    def moveRobot(self, speed: float, direction: float, twist: float):
        self.stickInputY = self.stick.getY()
        self.stickInputX = self.stick.getX()
        self.stickInputZ = self.stick.getZ()

        if (abs(self.stickInputY) < 0.2):
            self.realY = 0
        else:
            self.realY = self.stickInputY
        if (abs(self.stickInputX) < 0.2):
            self.realX = 0
        else:
            self.realX = self.stickInputX
        if (abs(self.stickInputZ) < 0.2):
            self.realZ = 0
        else: 
            self.realZ = self.stickInputZ

        self.MecanumDrive.driveCartesian(-self.realY, self.realX, self.realZ)
