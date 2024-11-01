import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int M = sc.nextInt();
		int N = sc.nextInt();
		int minPrime = 0;
		int sumPrime = 0;
		for (int i = N; i >= M; i--) {
			if (isPrime(i)) {
				sumPrime += i;
				minPrime = i;
			}
		}
		if (minPrime == 0) {
			System.out.println(-1);
		} else {
			System.out.println(sumPrime);
			System.out.println(minPrime);
		}
	}

	private static boolean isPrime(int n) {
		if (n == 1)
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
