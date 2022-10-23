import java.net.InetAddress;
import java.net.UnknownHostException;

public class Main {
    public static void main(String[] args) throws UnknownHostException {
        InetAddress start = InetAddress.getByName("192.168.0.1");
        InetAddress end = InetAddress.getByName("192.168.0.255");
        InetAddress current = start;
        while (!current.equals(end)) {
            System.out.println(current);
            byte[] address = current.getAddress();
            address[3]++;
            current = InetAddress.getByAddress(address);
        }
    }
}