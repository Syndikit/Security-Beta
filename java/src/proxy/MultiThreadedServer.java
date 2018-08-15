package proxy;

import java.io.*;
import java.net.*;

public class MultiThreadedServer implements Runnable{

    protected int serverPort = 1992;
    protected ServerSocket serverSocket = null;
    protected boolean running = true;
    protected Thread runningThread = null;

    public MultiThreadedServer(int port){
        this.serverPort = port;
    }

    @Override
    public void run(){
        synchronized(this){
            this.runningThread = Thread.currentThread();
        }
        openServerSocket();
        while (running) {
            Socket clientSocket = null;
            try {
                clientSocket = this.serverSocket.accept();
            } catch (IOException e) {
                if (!running) {
                    System.out.println("The server is stopped.");
                    return;
                }
                throw new RuntimeException("Error accepting client connection.", e);
            }
            new Thread(new ClientHandler(clientSocket, "Proxy Server.")).start();  
        }
        System.out.println("The server is stopped.");
    }

    private void openServerSocket(){
        try {
            this.serverSocket = new ServerSocket(this.serverPort);
        } catch (IOException e) {
            throw new RuntimeException("Cannot open port at " + this.serverPort);
        }
    }

    public synchronized void stop(){
        this.running = false;
        try {
            this.serverSocket.close();
        } catch (IOException e) {
            throw new RuntimeException("Error closing server socket.", e);
        }
    }
}