// Implementing MD5 in java

import java.security.MessageDigest;
import java.util.Scanner;

class MD5_Test {
    public static void main(String[] args) {

        String str;
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter your text: ");
        str = sc.nextLine();

        System.out.println("user input = " + str);

        byte[] msg = str.getBytes();
        byte[] hash = null;

        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            hash = md.digest(msg);

        } catch (Exception e) {
            e.printStackTrace();
        }

        StringBuilder strBuild = new StringBuilder();
        for (byte b : hash) {
            strBuild.append(String.format("%02x", b));
        }
        String strHash = strBuild.toString();
        System.out.println("The md5 hash is " + strHash);
    }
}