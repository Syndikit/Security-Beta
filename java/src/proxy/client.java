package proxy;

//Purpose: Establish a local Java client for testing encryption and message actions
// Imports vanilla Java networking and I/O packages
import java.net.*;
import java.io.*;

public class EClient {

    public EClient(String host, int port) {
        try {
            String serverHostName = new String("127.0.0.1");
            System.out.print("Connecting to host " + serverHostName + " on port " + port);

            Socket echoSocket = null;
            PrintWriter out = null;
            BufferedReader in = null;

            try {
                echoSocket = new Socket(serverHostName, 8081);
                out = new PrintWriter(echoSocket.getOutputStream(), true);
                in = new BufferedReader(new InputStreamReader(echoSocket.getInputStream()));
            } catch (UnknownHostException e) {
                System.err.println("Unknown host: " + serverHostName);
                System.exit(1);
            } catch (IOException e) {
                System.err.println("Unable to get streams from server");
                System.exit(1);
            }
            BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));

            while (true) {
                System.out.print("Client: ");
                String userInput = stdIn.readLine();

                if ("q".equalsIgnoreCase(userInput)) {
                    break;
                }
                out.println(userInput);
                System.out.println("server: " + in.readLine());
            }

            out.close();
            in.close();
            stdIn.close();
            echoSocket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }

    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 8081;
        new EClient(host, port);
    }
}