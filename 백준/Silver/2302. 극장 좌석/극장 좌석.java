import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int[] dp;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		dp = new int[n + 1];
		dp[0] = 1;
		dp[1] = 1;
		int prev = 0;
		int[] interval = new int[m + 1];
		for (int i = 0; i < m; i++) {
			int vip = sc.nextInt();
			interval[i] = (vip - prev - 1);
			prev = vip;
		}
		interval[m] = n - prev;
		Arrays.sort(interval);
		int res = 1;
		for (int i : interval) {
			res *= fibb(i);
		}
		System.out.println(res);

	}

	public static int fibb(int n) {
		if (dp[n] == 0) {
			dp[n] = fibb(n - 1) + fibb(n - 2);
		}
		return dp[n];
	}
}
