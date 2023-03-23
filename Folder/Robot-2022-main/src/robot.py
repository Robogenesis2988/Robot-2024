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
from vision import cameraLaunch
import ports


class Robot(wpilib.TimedRobot):
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        cameraLaunch()
        self.gyro = wpilib.ADXRS450_Gyro()
        self.gyro.calibrate()
        wpilib.SmartDashboard.putNumber('Gyro Angle', self.gyro.getAngle())
        #print('this port' + str(self.gyro.getPort()))
        #wpilib.SmartDashboard.putNumber('GyroAngle', self.gyro.getAngle())

        
        # self.solenoidDump = wpilib.DoubleSolenoid(
        #     wpilib.PneumaticsModuleType.CTREPCM, 1, 0)
        # self.solenoid2 = wpilib.DoubleSolenoid(
        #     wpilib.PneumaticsModuleType.CTREPCM, 3, 2)
        # self.solenoid3 = wpilib.DoubleSolenoid(
        #     wpilib.PneumaticsModuleType.CTREPCM, 5, 4)

        self.solenoidExtend = pneumatics.DoubleSolenoid(
            2,3)
        self.solenoidClamp = pneumatics.DoubleSolenoid(
            1,0)
        #self.solenoidClimb2 = pneumatics.DoubleSolenoid(
            #*ports.PneumaticPorts.CLIMB2)

        self.leftFront = wpilib.Talon(ports.MotorPorts.LEFT_FRONT)
        self.leftRear = wpilib.Talon(ports.MotorPorts.LEFT_REAR)
        self.rightFront = wpilib.Talon(ports.MotorPorts.RIGHT_FRONT)
        self.rightRear = wpilib.Talon(ports.MotorPorts.RIGHT_REAR)

        self.safeLock = 0

        #self.leftWinchMotor = wpilib.Talon(ports.MotorPorts.LEFT_WINCH)
        #self.rightWinchMotor = wpilib.Spark(ports.MotorPorts.RIGHT_WINCH)
        # self.rightWinchMotor.setInverted(True)

        #self.leftWinch = winch.Winch(self.leftWinchMotor)
        #self.rightWinch = winch.Winch(self.rightWinchMotor)

        # self.drive = wpilib.drive.MecanumDrive(self.leftFront, self.leftRear, self.rightFront, self.rightRear)

        self.drivetrain = drivetrain.MecanumDrive(
            self.leftFront, self.leftRear, self.rightFront, self.rightRear)
        self.drivetrain.rightInverted(False)
        self.drivetrain.leftInverted(True)
        self.drivetrain.setDeadzone(0.5, 0.5)
        self.drivetrain.speedMultiplier = 1
        self.drivetrain.twistMultiplier = 1

        

        # self.rightFront.setInverted(True)
        # self.rightRear.setInverted(True)
        # self.leftFront.setInverted(True)
        # self.leftRear.setInverted(True) I would keep this commented out unless it drives in the wrong direction then you can revise.

        self.stick = wpilib.Joystick(ports.JoystickPorts.JOY)

        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()
        self.gyro.calibrate()
        # autonomous.autonomousInit()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        if (self.timer.get() < 1.5):
            #self.drivetrain.(self.realY, -self.realZ, -self.realX)
            self.solenoidClamp.close()
            self.solenoidExtend.open()
            #self.drivetrain.moveRobot(.6, 0, 0)
            #self.leftFront.set(0.6)
            #self.leftRear.set(0.6)
            #self.rightFront.set(0.6)
            #self.rightRear.set(0.6)
        #elif (self.timer.get() > 1.5 and self.timer.get() < 2.5):
            #self.solenoidExtend.open()
        #elif (self.timer.get() > 3 & self.timer.get() < 3.5):
            #self.solenoidExtend.close()
        elif ((self.timer.get() > 1.5) and (self.timer.get() < 2.7)):
            #self.solenoidExtend.close()
           #self.MecanumDrive.driveCartesian(self.realY, -self.realZ, -self.realX)
            #self.solenoidClamp.open()
            self.drivetrain.moveRobot(-.6, 0,0)
            self.leftFront.set(0.6)
            self.leftRear.set(0.6)
            self.rightFront.set(0.6)
            self.rightRear.set(0.6)
            if self.timer.get() > 2.25 and self.timer.get() < 3:
                self.solenoidExtend.close()
        #elif (self.timer.get() > 3.5 and self.timer.get() < 15):
            #while (self.gyro.getAngle() < 3):
            #    self.leftFront.set(.2)
            #    self.leftFront.set(.2)
            #    self.rightFront.set(.2)
        
        else:
            self.drivetrain.moveRobot(0, 0,0)
            self.leftFront.set(0)
            self.leftRear.set(0)
            self.rightFront.set(0)
            self.rightRear.set(0)

    def teleopInit(self) -> None:
        self.timer.reset()
        self.timer.start()
        

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""

        # Toggle pistons on button 3
        wpilib.SmartDashboard.putNumber('Gyro Angle', self.gyro.getAngle())
        if self.safeLock == 0 and self.stick.getRawButtonPressed(ports.JoystickButtons.EXTENDTOGGLE):
            self.solenoidExtend.toggle()

        if self.stick.getRawButtonPressed(ports.JoystickButtons.CLAMPTOGGLE):
            self.solenoidClamp.toggle()

        if self.solenoidClamp.getState() == False:
            self.safeLock = 1
        else:
            self.safeLock = 0

        if self.stick.getRawButtonPressed(11):
            if self.gyro.getAngle() > 1:
                self.leftFront.set(.5)


        # Toggle speed multiplier on button 2
        if self.stick.getRawButtonPressed(ports.JoystickButtons.SPEEDMULTIPLIER):
            if self.drivetrain.speedMultiplier == 1:
                self.drivetrain.speedMultiplier = 0.5
            else:
                self.drivetrain.speedMultiplier = 1

        self.drivetrain.drive(self.stick)


if __name__ == "__main__":
    wpilib.run(Robot)