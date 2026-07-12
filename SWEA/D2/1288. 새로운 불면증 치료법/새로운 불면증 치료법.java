import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= TC; tc++) {
            int N = Integer.parseInt(br.readLine());
            int i = 1;
            Set<Integer> numSet = new HashSet<>();
            while (numSet.size() < 10) {
                for (char c : Integer.toString(N * i).toCharArray()) {
                    numSet.add(c - '0');
                }
                i++;
            }
            System.out.printf("#%d %d\n", tc, (i - 1) * N);

        }
    }
}
