import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();
        
        int[] divisors = new int[count];

        for (int i = 0; i < count; i++) {
            divisors[i] = sc.nextInt();
        }

        Arrays.sort(divisors);

        long N = (long) divisors[0] * divisors[count - 1];

        System.out.println(N);

        sc.close();
    }
}