package org.usfirst.frc.team5483.robot.commands;

import org.usfirst.frc.team5483.robot.Robot;
import org.usfirst.team5483.robot.vision.Receiver;

import edu.wpi.first.wpilibj.command.Command;

public class GoToPeg extends Command {
	protected boolean isFinished() {
		return false;
	}

	public void execute() {
		if (Receiver.receiving) {
			if (Receiver.wRight - 10 > Receiver.wLeft) {
				Robot.chassis.tankDrive(0, 1);
			} else if (Receiver.wRight + 10 < Receiver.wLeft) {
				Robot.chassis.tankDrive(1, 0);
			} else if (Receiver.x > Receiver.middle) {
				Robot.chassis.middleDrive(-1);
			} else if (Receiver.x < Receiver.middle) {
				Robot.chassis.middleDrive(1);
			}
		}

	}

}
