package proxy;

import java.io.*;
import java.net.*;

public class ProxyServer extends Thread {

    // Sets a constant value for the port number and instantiates a Socket called
    // socket (original, I know...) to be used in main method

	private static final Boolean RUNNING = true;
    private static final int PORT_NUMBER = 8081;
    Socket socket;

    private ProxyServer(Socket socket) {
        this.socket = socket;
        System.out.print("Connected to client at: " + socket.getInetAddress().getHostAddress());
        start();
    }

    @Override
    public void run() {
        // Instantiates Input and Output streams, and a BufferedReader to read the
        // streams the ProxyServer will receive from and send to EClient
        InputStream input = null;
        OutputStream output = null;

        try {
            input = socket.getInputStream();
            output = socket.getOutputStream();

            BufferedReader reader = new BufferedReader(new InputStreamReader(input));
            String request;

            while ((request = reader.readLine()) != null) {
                System.out.println("Message received! " + request);
                request += '\n';
                output.write(request.getBytes());
            }
        } catch (IOException e) {
            System.out.println("Unable to get streams from EClient.");
        } 
        finally {
            try {
                input.close();
                output.close();
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) throws IOException{
        ServerSocket serv = new ServerSocket(PORT_NUMBER);
    }
}