I'm trying to create a MITM proxy over SSL. I'm using the following code:
<code>import socket
import ssl

def main():
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

    bindsocket = socket.socket()
    bindsocket.bind(('', 443))
    bindsocket.listen(5)

    while True:
        newsocket, fromaddr = bindsocket.accept()
        conn = context.wrap_socket(newsocket, server_side=True)
        try:
            deal_with_client(conn)
        finally:
            conn.shutdown(socket.SHUT_RDWR)
            conn.close()

def deal_with_client(conn):
    data = conn.recv(1024)
    print(data)

if __name__ == '__main__':
    main()
</code>
I'm using the following command to generate the certificate:
<code>openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
</code>
I'm using the following command to connect to the proxy:
<code>curl --proxy https://localhost:443 https://www.google.com
</code>
The problem is that the <code>wrap_socket</code> call hangs. I've tried using <code>context.check_hostname = False</code> and <code>context.verify_mode = ssl.CERT_NONE</code> but it still hangs.
I've also tried using <code>context.verify_mode = ssl.CERT_REQUIRED</code> and <code>context.check_hostname = True</code> but it still hangs.
I've also tried using <code>context.verify_mode = ssl.CERT_REQUIRED</code> and <code>context.check_hostname = False</code> but it still hangs.
I've also tried using <code>context.