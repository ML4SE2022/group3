I'm trying to create a MITM proxy over SSL. I'm using the following code:
<code>import socket
import ssl

def mitm_proxy(client_socket, server_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        server_socket.sendall(data)
        data = server_socket.recv(1024)
        if not data:
            break
        client_socket.sendall(data)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 8443))
    server_socket.listen(5)
    while True:
        client_socket, addr = server_socket.accept()
        print('Got connection from', addr)
        server_socket = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        server_socket.connect(('localhost', 8443))
        mitm_proxy(client_socket, server_socket)

if __name__ == '__main__':
    main()
</code>
I'm using the following Java code to connect to the proxy:
<code>import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

import javax.net.ssl.SSLSocketFactory;

public class Client {

    public static void main(String[] args) throws UnknownHostException, IOException {
        Socket socket = SSLSocketFactory.getDefault().createSocket("localhost", 8443);
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in));
        String userInput;
        while ((userInput = stdIn.readLine())