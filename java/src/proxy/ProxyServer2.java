package proxy;

import java.io.*;
import java.net.*;

public class ProxyServer2 extends Thread{

    private ServerSocket server;

    Socket socket;

    private ProxyServer2(Socket socket){
        this.socket = socket;
        
        start();
    }

    public void listen() throws Exception{

        String data = null;
        socket = this.server.accept();
        System.out.println("Connected to client at: " + socket.getInetAddress().getHostAddress());

        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
    }
}
