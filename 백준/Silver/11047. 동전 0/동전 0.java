import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		int[] coins = new int[N];
		for (int i = 0; i < N; i++) {
			coins[i] = sc.nextInt();
		}
		int ans = 0;
		while (N > 0 && K > 0) {
			ans += K / coins[N - 1];
			K %= coins[N - 1];
			N -= 1;
		}
		System.out.println(ans);
	}
}
