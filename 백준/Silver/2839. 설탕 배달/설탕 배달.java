import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    int n = scanner.nextInt();
    scanner.close();

    int count1 = n/5;
    int count2 = n%5;

    while (count1 >= 0) {
        if(count2%3 == 0){
            System.out.println(count1+(count2/3));
            return;
        }
        count1--;
        count2 += 5;
    }
    System.out.println(-1);
  }
}