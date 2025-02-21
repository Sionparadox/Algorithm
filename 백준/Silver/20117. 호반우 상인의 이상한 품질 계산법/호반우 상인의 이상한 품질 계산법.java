import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		Integer[] ho = new Integer[N];
		for (int i = 0; i < N; i++) {
			ho[i] = sc.nextInt();
		}
		Arrays.sort(ho, (a, b) -> b - a);
		int res = 0;
		for (int i = 0; i < N / 2; i++) {
			res += ho[i] * 2;
		}
		if (N % 2 == 1)
			res += ho[N / 2];
		System.out.println(res);
	}
}
