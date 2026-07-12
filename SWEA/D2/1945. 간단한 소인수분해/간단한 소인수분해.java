import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] primes = new int[] { 2, 3, 5, 7, 11 };
        int TC = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= TC; tc++) {
            int N = Integer.parseInt(br.readLine());
            int[] answer = new int[] { 0, 0, 0, 0, 0 };
            for (int i = 0; i < 5; i++) {
                while (N % primes[i] == 0) {
                    answer[i]++;
                    N /= primes[i];
                }
            }

            System.out.printf("#%d %d %d %d %d %d\n", tc, answer[0], answer[1], answer[2], answer[3], answer[4]);
        }

    }
}