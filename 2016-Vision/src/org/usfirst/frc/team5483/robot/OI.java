package org.usfirst.frc.team5483.robot;

import org.usfirst.frc.team5483.robot.commands.ClimbRope;
import org.usfirst.frc.team5483.robot.commands.GrabBalls;

import edu.wpi.first.wpilibj.Joystick;
import edu.wpi.first.wpilibj.buttons.Button;
import edu.wpi.first.wpilibj.buttons.JoystickButton;

public class OI {
	
	//Joysticks
	private static final Joystick leftStick = new Joystick(RobotMap.lStickPort);
	private static final Joystick rightStick = new Joystick(RobotMap.rStickPort);
	
	public OI() {
		
		//Buttons - port #s are subject to change when tested
		final JoystickButton r_trigger = new JoystickButton(rightStick, 1);
		final JoystickButton r_butt_4 = new JoystickButton(rightStick, 4);
		
		final JoystickButton l_trigger = new JoystickButton(leftStick, 1);
		final JoystickButton l_butt_2 = new JoystickButton(leftStick, 2);
		final JoystickButton l_butt_3 = new JoystickButton(leftStick, 3);
		
		l_butt_2.whileHeld(new ClimbRope());
		l_butt_3.whileHeld(new GrabBalls());
	}
	
	public Joystick getLeftStick() {
		return leftStick;
	}
	
	public Joystick getRightStick() {
		return rightStick;
	}
}
