import java.net.URI;
import java.net.URISyntaxException;
public class WebAddressParser{
    public static void main(String[] args){
        parseAddress("foo://example.com:8042/over/there?name=ferret#nose");
        parseAddress("urn:example:animal:ferret:nose");
    }

    static void parseAddress(String a){
        System.out.println("Parsing " + a);
        try{

            // this line does the work
            URI u = new URI(a);

            System.out.println("\tscheme = " + u.getScheme());
            System.out.println("\tdomain = " + u.getHost());
            System.out.println("\tport = " + (-1==u.getPort()?"default":u.getPort()));
            System.out.println("\tpath = " + (null==u.getPath()?u.getSchemeSpecificPart():u.getPath()));
            System.out.println("\tquery = " + u.getQuery());
            System.out.println("\tfragment = " + u.getFragment());
        }
        catch (URISyntaxException x){
            System.err.println("Oops: " + x);
        }
    }
}