import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int cnt = 0;
		while (sum(cnt) * 6 + 1 < n) {
			cnt++;
		}
		System.out.println(++cnt);
	}

	private static int sum(int n) {
		int res = 0;
		for (int i = 1; i <= n; i++) {
			res += i;
		}
		return res;
	}
}