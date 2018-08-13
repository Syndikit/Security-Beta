// Purpose: Establish a local Java server for testing encryption and message actions
// Imports vanilla Java networking and I/O packages
import java.net.*;
import java.io.*;

public class EServer extends Thread {

    // Sets port 8081 as immutable port to be used in Main()
    public static final int PORT_NUMBER = 8081;
    protected Socket socket;

    private EServer(Socket socket)
    {
        this.socket = socket;
        System.out.println("New client connected from: " + socket.getInetAddress().getHostAddress());
        start();
    }

    /* 
    Creates input and output streams, checks whether messages come through, and closes streams and socket upon completion. 
    Catches and throws IOExceptions and prints to console
    */
    public void run()
    {
        InputStream input = null;
        OutputStream output = null;

        try 
        {
            input = socket.getInputStream();
            output = socket.getOutputStream();

            BufferedReader reader = new BufferedReader(new InputStreamReader(input));

            String request;

            while ((request = reader.readLine()) != null) 
            {
                System.out.println("Message received! " + request);
                request += '\n';
                output.write(request.getBytes());
            }
        } 
        catch (IOException e) 
        {
            System.out.println("Unable to get streams from client.");
        }
        finally
        {
            try {
                input.close();
                output.close();
                socket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String args[]) throws IOException {
        System.out.println("Server for Proxy");
        ServerSocket serv = null;
        try {
            serv = new ServerSocket(PORT_NUMBER);
            while (true) {
                new EServer(serv.accept());
            }
            
        } catch (IOException e) {
            System.out.println("Cannot start server.");
        }finally{
            try {
                if(serv != null){
                    serv.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        
    }
    
}

