package org.usfirst.frc.team5483.robot.commands;

import org.usfirst.frc.team5483.robot.Robot;

import edu.wpi.first.wpilibj.command.Command;

public class GrabBalls extends Command {
	
	public GrabBalls() {
		requires(Robot.ballGrabber);
	}
	
	@Override
	public void execute() {
		Robot.ballGrabber.spinGrabber();
	}
	
	@Override
	protected boolean isFinished() {
		return false;
	}

}
