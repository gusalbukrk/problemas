import java.util.Scanner;

public class ProblemaD {
    public static void main(String[] args) {
        int[] letras = new int[26];
        int ans = 0;
        Scanner scanner = new Scanner(System.in);
        String p1 = scanner.next();
        String p2 = scanner.next();
        
        for (int i = 0; i < p1.length(); i++) {
            letras[p1.charAt(i) - 'a']++;
        }
        
        for (int i = 0; i < p2.length(); i++) {
            letras[p2.charAt(i) - 'a']++;
        }
        
        for (int count : letras) {
            if (count > ans) {
                ans = count;
            }
        }
        
        if (ans < 3) {
            System.out.println("SIM");
        } else {
            System.out.println("NAO");
        }
    }
}
