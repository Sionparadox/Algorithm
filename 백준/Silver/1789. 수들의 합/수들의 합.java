import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		long S = sc.nextLong();
		int ans = 1;
		while (S >= ans) {
			S -= ans++;
		}

		System.out.println(--ans);
	}
}
