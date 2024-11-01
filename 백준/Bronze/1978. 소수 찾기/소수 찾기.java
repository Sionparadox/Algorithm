import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();

		int cnt = 0;
		for (int i = 0; i < n; i++) {
			if (isPrime(sc.nextInt())) {
				cnt += 1;
			}
		}
		System.out.println(cnt);

	}

	private static boolean isPrime(int n) {
		if (n <= 1)
			return false;
		if (n == 2)
			return true;
		for (int i = 2; i < Math.sqrt(n) + 1; i++) {
			if (n % i == 0) {
				return false;
			}
		}
		return true;
	}
}
