package proxy;

import java.io.*;
import java.net.*;
import proxy.ProxyServer;
import proxy.EClient;

public class Main {

    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 8081;
        EClient client = new EClient(host, port);
        ProxyServer server = new ProxyServer();

    }
}
