import java.security.SecureRandom;
import java.util.Scanner;

public class Main {
    private static final String UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final String LOWER = "abcdefghijklmnopqrstuvwxyz";
    private static final String DIGITS = "0123456789";
    private static final String SPECIAL = "!@#$%^&*()-_=+[]{}|;:,.<>?";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Password length: ");
        int length = scanner.nextInt();
        System.out.print("Include uppercase letters? (y/n): ");
        boolean useUpper = scanner.next().equalsIgnoreCase("y");
        System.out.print("Include lowercase letters? (y/n): ");
        boolean useLower = scanner.next().equalsIgnoreCase("y");
        System.out.print("Include digits? (y/n): ");
        boolean useDigits = scanner.next().equalsIgnoreCase("y");
        System.out.print("Include special characters? (y/n): ");
        boolean useSpecial = scanner.next().equalsIgnoreCase("y");

        String password = generatePassword(length, useUpper, useLower, useDigits, useSpecial);
        System.out.println("Generated password: " + password);
    }

    public static String generatePassword(int length, boolean useUpper, boolean useLower, boolean useDigits, boolean useSpecial) {
        StringBuilder charPool = new StringBuilder();
        if (useUpper) charPool.append(UPPER);
        if (useLower) charPool.append(LOWER);
        if (useDigits) charPool.append(DIGITS);
        if (useSpecial) charPool.append(SPECIAL);

        if (charPool.length() == 0 || length <= 0) {
            throw new IllegalArgumentException("No character types selected or invalid length.");
        }

        SecureRandom random = new SecureRandom();
        StringBuilder password = new StringBuilder(length);
        for (int i = 0; i < length; i++) {
            int idx = random.nextInt(charPool.length());
            password.append(charPool.charAt(idx));
        }
        return password.toString();
    }
}