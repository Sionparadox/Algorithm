import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int t = 0; t < T; t++) {
			System.out.println(solve(sc));
		}
		sc.close();

	}

	private static int solve(Scanner sc) {
		int N = sc.nextInt();
		int[] grades = new int[N + 1];
		for (int i = 0; i < N; i++) {
			int idx = sc.nextInt();
			grades[idx] = sc.nextInt();
		}

		int minGrade = grades[1];
		int ans = 1;
		for (int i = 1; i < N + 1; i++) {
			if (grades[i] < minGrade) {
				minGrade = grades[i];
				ans++;
			}
		}
		return ans;

	}
}
