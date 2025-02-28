import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] A = new int[n];
		for (int i = 0; i < n; i++) {
			A[i] = sc.nextInt();
		}
		int m = sc.nextInt();
		int[] B = new int[m];
		for (int i = 0; i < m; i++) {
			B[i] = sc.nextInt();
		}

		int limit = (int)Math.sqrt(Math.max(Arrays.stream(A).max().getAsInt(), Arrays.stream(B).max().getAsInt()));
		boolean[] isPrime = new boolean[limit + 1];
		Arrays.fill(isPrime, true);
		isPrime[0] = false;
		isPrime[1] = false;
		for (int i = 2; i < Math.sqrt(limit) + 1; i++) {
			if (isPrime[i]) {
				for (int j = i * i; j < limit + 1; j += i) {
					isPrime[j] = false;
				}
			}
		}

		HashMap<Integer, Integer> factorA = new HashMap<>();
		HashMap<Integer, Integer> factorB = new HashMap<>();

		for (int i = 2; i < limit + 1; i++) {
			if (isPrime[i]) {
				for (int x = 0; x < n; x++) {
					while (A[x] % i == 0) {
						factorA.put(i, factorA.getOrDefault(i, 0) + 1);
						A[x] /= i;
					}
				}
				for (int y = 0; y < m; y++) {
					while (B[y] % i == 0) {
						factorB.put(i, factorB.getOrDefault(i, 0) + 1);
						B[y] /= i;
					}
				}
			}
		}

		for (int a : A) {
			if (a != 1) {
				factorA.put(a, factorA.getOrDefault(a, 0) + 1);
			}
		}
		for (int b : B) {
			if (b != 1) {
				factorB.put(b, factorB.getOrDefault(b, 0) + 1);
			}
		}

		long res = 1;
		boolean overflow = false;

		for (int i : factorA.keySet()) {
			if (factorB.containsKey(i)) {
				int power = Math.min(factorA.get(i), factorB.get(i));
				for (int j = 0; j < power; j++) {
					res *= i;
					if (res > 999999999) {
						overflow = true;
						res %= 1000000000;
					}
				}
			}
		}

		if (overflow) {
			System.out.printf("%09d%n", res % 1000000000);
		} else {
			System.out.println(res);
		}
	}
}
