package proxy;

import java.io.*;
import java.net.*;

public class Main {

    public static void main(String[] args) {
        /*
         * String host = "127.0.0.1"; int port = 8081; EClient client = new
         * EClient(host, port); ProxyServer server = new ProxyServer();
         */

        MultiThreadedServer server = new MultiThreadedServer(9000);
        new Thread(server).start();

        try {
            Thread.sleep(20 * 1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Server is stopping");
        server.stop();
    }
}
