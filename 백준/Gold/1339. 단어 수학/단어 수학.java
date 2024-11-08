import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String[] strings = new String[n];
		Integer[] letters = new Integer[26];
		Arrays.fill(letters, 0);
		for (int i = 0; i < n; i++) {
			strings[i] = sc.next();
			for (int j = 0; j < strings[i].length(); j++) {
				letters[strings[i].charAt(j) - 'A'] += (int)Math.pow(10, strings[i].length() - j - 1);
			}
		}
		int ans = 0;
		Arrays.sort(letters, (a, b) -> b - a);
		for (int i = 0; i < 10; i++) {
			ans += letters[i] * (9 - i);
		}
		System.out.println(ans);
	}
}
