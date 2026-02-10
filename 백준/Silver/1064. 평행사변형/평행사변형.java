import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String Point = br.readLine();

    StringTokenizer st = new StringTokenizer(Point);

    double Ax = Integer.parseInt(st.nextToken());
    double Ay = Integer.parseInt(st.nextToken());
    double Bx = Integer.parseInt(st.nextToken());
    double By = Integer.parseInt(st.nextToken());
    double Cx = Integer.parseInt(st.nextToken());
    double Cy = Integer.parseInt(st.nextToken());

    if ((By - Ay) * (Cx - Bx) == (Cy - By) * (Bx - Ax)) {
      System.out.println("-1.0");
      return;
    }

    double len1 = Math.pow(Ax - Bx, 2) + Math.pow(Ay - By, 2);
    double len2 = Math.pow(Ax - Cx, 2) + Math.pow(Ay - Cy, 2);
    double len3 = Math.pow(Bx - Cx, 2) + Math.pow(By - Cy, 2);

    double[] lens = {len1, len2, len3};
    Arrays.sort(lens);

    double max = (Math.sqrt(lens[2]) + Math.sqrt(lens[1])) * 2;
    double min = (Math.sqrt(lens[1]) + Math.sqrt(lens[0])) * 2;

    System.out.println(max - min);
  }
}