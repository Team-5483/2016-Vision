package org.usfirst.frc.team5483.robot.subsystems;

import edu.wpi.first.wpilibj.Talon;
import edu.wpi.first.wpilibj.command.Subsystem;

public class Climber extends Subsystem {
	
	private static final Talon winchMotor = new Talon(9);
	
	public boolean stopped = false;

	@Override
	protected void initDefaultCommand() {
	}
	
	public void climbRope() {
		winchMotor.set(1);
	}
	
	public void climbDisable() {
		winchMotor.disable();
		stopped = true;
	}
	
	public boolean isStopped() {
		return stopped;
	}
}
