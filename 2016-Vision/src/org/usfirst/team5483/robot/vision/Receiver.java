package org.usfirst.team5483.robot.vision;
import java.io.IOException;
import java.net.*;

public class Receiver implements Runnable{
	public static final int PORT = 7070;
	public static int x = 0,y = 0 ,wRight = 0, wLeft = 0;
	public static final int middle = 300;
	public static boolean receiving = false;
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
            	  wLeft = Integer.parseInt(strArray[2]);
            	  wRight = Integer.parseInt(strArray[3]);
            	  receiving = true;
              } else {
            	  receiving = false;
              }
              System.out.println("x : " + x + " y : " + y);

        }
      } catch (IOException e) {
              System.out.println(e);
      }
    }

	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

    
}