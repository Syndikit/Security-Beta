package proxy;

//Purpose: Establish a local Java client for testing encryption and message actions
// Imports vanilla Java networking and I/O packages
import java.net.*;
import java.io.*;

public class EClient{

    public EClient(String host, int port){
        try {
            String serverHostName = new String ("127.0.0.1");
        } catch (Exception e) {
            //TODO: handle exception
        }
    }
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 8081;
        new EClient(host, port); 
    }
}