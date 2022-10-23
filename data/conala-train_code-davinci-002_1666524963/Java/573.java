import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class Decrypt {
    public static void main(String[] args) throws Exception {
        String key = "1234567890123456";
        String iv = "1234567890123456";
        String encrypted = "c2VuZGluZyBhIG1lc3NhZ2U=";
        String decrypted = decrypt(encrypted, key, iv);
        System.out.println(decrypted);
    }

    public static String decrypt(String encrypted, String key, String iv) throws Exception {
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
        SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes("UTF-8"), "AES");
        IvParameterSpec ivParameterSpec = new IvParameterSpec(iv.getBytes("UTF-8"));
        cipher.init(Cipher.DECRYPT_MODE, secretKeySpec, ivParameterSpec);
        byte[] decodedEncryptedData = Base64.getDecoder().decode(encrypted);
        byte[] original = cipher.doFinal(decodedEncryptedData);
        return new String(original);
    }
}