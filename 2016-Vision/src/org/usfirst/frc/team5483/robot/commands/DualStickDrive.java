package org.usfirst.frc.team5483.robot.commands;

import org.usfirst.frc.team5483.robot.Robot;

import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.command.Command;

public class DualStickDrive extends Command {
	
	private Joystick leftStick;
	private Joystick rightStick;
	
	public DualStickDrive() {
		requires(Robot.chassis);
		
		if(Robot.oi.getLeftStick() != null) {
			leftStick = Robot.oi.getLeftStick();
			rightStick = Robot.oi.getRightStick();
		} else {
			System.err.println("Error in DualStickDrive: Initialize OI first!");
			System.exit(1);
		}
	}
	
	@Override
	public void execute() {
		Robot.chassis.tankDrive(leftStick.getY(), rightStick.getY());
	}
	
	@Override
	protected boolean isFinished() {
		return false;
	}
	
}
