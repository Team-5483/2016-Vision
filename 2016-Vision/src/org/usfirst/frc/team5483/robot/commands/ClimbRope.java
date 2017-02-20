package org.usfirst.frc.team5483.robot.commands;

import org.usfirst.frc.team5483.robot.Robot;

import edu.wpi.first.wpilibj.command.Command;
import edu.wpi.first.wpilibj.Talon;

public class ClimbRope extends Command {
	
	public ClimbRope() {
		requires(Robot.climber);
	}
	
	@Override
	public void execute() {
		Robot.climber.climbRope();
	}
	
	@Override
	protected boolean isFinished() {
		return false;
	}

}
