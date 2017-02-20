package org.usfirst.team5483.robot.vision;
import java.io.IOException;
import java.net.*;

public class Receiver implements Runnable{
	public static final int PORT = 7070;
	public int x = 0,y = 0;
	public void run() {
        new Receiver().getPacket(PORT);
	}

    public void getPacket(int port) {    
      try {
        DatagramSocket serverSocket = new DatagramSocket(port);
        byte[] receiveData = new byte[8];

        System.out.printf("Listening on udp:%s:%d%n",
                InetAddress.getLocalHost().getHostAddress(), port);     
        DatagramPacket receivePacket = new DatagramPacket(receiveData,
                           receiveData.length);

        while(true)
        {
              serverSocket.receive(receivePacket);
              String sentence = new String( receivePacket.getData(), 0,
                                 receivePacket.getLength() );
              if(sentence.startsWith("P:")) {
            	  String[] strArray = sentence.substring(1).split(" ");
            	  x = Integer.parseInt(strArray[0]);
            	  y = Integer.parseInt(strArray[1]);
              }
              System.out.println("x : " + x + " y : " + y);

              /*
              InetAddress IPAddress = receivePacket.getAddress();
              String sendString = "polo";
              byte[] sendData = sendString.getBytes("UTF-8");
              DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length,
                   IPAddress, receivePacket.getPort());
              serverSocket.send(sendPacket);
              
              */
        }
      } catch (IOException e) {
              System.out.println(e);
      }
      // should close serverSocket in finally block
    }

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

    
}