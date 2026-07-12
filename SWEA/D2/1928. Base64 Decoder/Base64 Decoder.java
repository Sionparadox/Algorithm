import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= TC; tc++) {
            String S = br.readLine();

            StringBuilder answer = new StringBuilder();
            int buffer = 0;
            int bitsLeft = 0;

            for (char c : S.toCharArray()) {

                int value = decode(c);

                buffer = (buffer << 6) | value;
                bitsLeft += 6;

                if (bitsLeft >= 8) {
                    bitsLeft -= 8;
                    int b = (buffer >> bitsLeft) & 0xFF;
                    answer.append((char) b);
                }
            }

            System.out.printf("#%d %s\n", tc, answer.toString());
        }
    }

    static int decode(char x) {
        if (x >= 'A' && x <= 'Z')
            return x - 'A';
        if (x >= 'a' && x <= 'z')
            return x - 'a' + 26;
        if (x >= '0' && x <= '9')
            return x - '0' + 52;
        return x == '+' ? 62 : 63;
    }
}