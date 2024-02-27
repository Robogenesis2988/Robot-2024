class MotorPorts():
    # Drivetrain motors
    LEFT_FRONT = 1
    LEFT_REAR = 0
    RIGHT_FRONT = 3
    RIGHT_REAR = 2

    # Winch motors
    LEFT_WINCH = 5
    RIGHT_WINCH = 4


class PneumaticPorts():
    # Used Ports: 0,1,2,3,7,6
    EXTEND = (1, 0)
    CLAMP = (2, 3)
    CLIMB2 = (6, 7)


class JoystickPorts():
    JOY = 0


class JoystickButtons():
    
    WINCHEXTEND = 6
    WINCHRETRACT = 4
    GUNSHOOTERGUNBUTTON = 1
    GUNINTAKERGUNBUTTON = 2
    SPEEDMULTIPLIER = 3
