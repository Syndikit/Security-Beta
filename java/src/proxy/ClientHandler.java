package proxy;

import java.io.*;
import java.net.*;

public class ClientHandler implements Runnable{

    protected Socket clientSocket = null;
    protected String serverText = null;
    protected String responseText = null;

    public ClientHandler(Socket clientSocket, String serverText){
        this.clientSocket = clientSocket;
        this.serverText = serverText;
        this.responseText = ("HTTP/1.1 200 OK\n\nClientHandler: " + this.serverText + " - ");
    }

    public void run(){

        try {
            InputStream input = clientSocket.getInputStream();
            OutputStream output = clientSocket.getOutputStream();
            long currentTime = System.currentTimeMillis();
            output.write((responseText + currentTime).getBytes());
            output.close();
            input.close();
            System.out.println("Request processed at: " + currentTime);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}