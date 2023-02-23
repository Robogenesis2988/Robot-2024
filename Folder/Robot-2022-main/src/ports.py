class MotorPorts():
    # Drivetrain motors
    LEFT_FRONT = 1
    LEFT_REAR = 2
    RIGHT_FRONT = 3
    RIGHT_REAR = 4

    # Winch motors
    LEFT_WINCH = 7
    RIGHT_WINCH = 6


class PneumaticPorts():
    # Used Ports: 0,1,2,3,7,6
    DUMP = (1, 0)
    CLIMB1 = (2, 3)
    CLIMB2 = (6, 7)


class JoystickPorts():
    JOY = 0


class JoystickButtons():
    WINCHEXTEND = 6
    WINCHRETRACT = 4
    CLIMBPISTONTOGGLE = 5
    DUMPTOGGLE = 3
    SPEEDMULTIPLIER = 2
