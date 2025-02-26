import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Integer[] cust = new Integer[n];
		for (int i = 0; i < n; i++) {
			cust[i] = sc.nextInt();
		}
		Arrays.sort(cust, (a, b) -> b - a);
		long res = 0;
		for (int i = 0; i < n; i++) {
			res += Math.max(cust[i] - i, 0);
		}
		System.out.println(res);
	}
}
