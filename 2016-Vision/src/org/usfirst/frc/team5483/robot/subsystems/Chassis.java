package org.usfirst.frc.team5483.robot.subsystems;

import org.usfirst.frc.team5483.robot.commands.DualStickDrive;

import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.RobotDrive;
import edu.wpi.first.wpilibj.Spark;
import edu.wpi.first.wpilibj.Talon;
import edu.wpi.first.wpilibj.command.Subsystem;

public class Chassis extends Subsystem {
	
	private static Spark frontLeftController;
	private static Spark frontRightController;
	private static Spark rearLeftController;
	private static Spark rearRightController;
	
	private static Talon middleController;
	
	private static RobotDrive robotDrive;

	public Chassis() {
		frontLeftController = new Spark(0);
		frontRightController = new Spark(2);
		rearLeftController = new Spark(3);
		rearRightController = new Spark(4);
		
		middleController = new Talon(5);
		
		robotDrive = new RobotDrive(frontLeftController, rearLeftController,
				frontRightController, rearRightController);
	}
	
	public void tankDrive(double left, double right) {
		robotDrive.tankDrive(left, right);
	}
	
	//someone write me
	public void tankHDrive(double left, double right, double rot) {
		robotDrive.tankDrive(left, right);
	}
	
	public void middleDrive(double x) {
		middleController.set(x);
	}
	
	@Override
	protected void initDefaultCommand() {
		setDefaultCommand(new DualStickDrive());
	}

}
