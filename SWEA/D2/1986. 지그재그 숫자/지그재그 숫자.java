import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= TC; tc++) {
            int N = Integer.parseInt(br.readLine());
            int answer = N % 2 == 0 ? -N / 2 : N - N / 2;
            System.out.printf("#%d %d\n", tc, answer);
        }
    }
}
