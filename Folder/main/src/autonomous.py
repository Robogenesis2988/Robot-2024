import wpilib
import wpilib.drive

from drivetrain import DriveTrain

"""
This won't be called in the robot.py file unless you decide to replace the robot.py autonomous with
calling functions from this autonomous either way works we're just not really using this autonomous.
"""

timer = wpilib.Timer

def autonomousInitialization():
    """
    This function is called once at the start of Autonomous.
    This can be used to start the timer.
    """
    timer.reset()
    timer.start()

def autonomousPeriodicCommands(drive: DriveTrain):
    """
    This function is called periodically (every 1 bajillionith of a second (not literally)).
    This is where the movement for autonomous should be programmed.
    """
    if timer.get() < 1.5:
        drive.drivePolar(.25,0,0) #drives foward for one second at 1/4 speed
    else:
        drive.drivePolar(0,0,0)

# # class TimedAutonomous():
# #     auto_actions = []

# #     class Action():
# #         class ActionType(Enum):
# #             SingleAction = auto()
# #             ContiniousAction = auto()

# #         def __init__(self, type: ActionType) -> None:
# #             type = type

# #     def __init__(self) -> None:
# #         timer = wpilib.Timer()

# #     def autonomousInit(self):
# #         timer.reset()
# #         timer.start()

# #     def autonomousPeriodic(self):
# #         pass

# #     def SingleAction(self, startTime: int, action: function):
# #         """
# #         startTime (in milliseconds)
# #         action - The function to run
# #         """
# #         auto_actions.append((startTime, action))
