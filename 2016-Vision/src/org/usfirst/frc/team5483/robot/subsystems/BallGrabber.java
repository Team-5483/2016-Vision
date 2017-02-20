package org.usfirst.frc.team5483.robot.subsystems;

import edu.wpi.first.wpilibj.Talon;
import edu.wpi.first.wpilibj.command.Subsystem;

public class BallGrabber extends Subsystem {

	private Talon grabberMotor;
	
	public BallGrabber() {
		grabberMotor = new Talon(8);
	}
	
	public void spinGrabber() {
		grabberMotor.set(1);
	}
	
	@Override
	protected void initDefaultCommand() {
	}
	
}
