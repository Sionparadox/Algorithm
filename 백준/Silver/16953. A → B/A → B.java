import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int ans = 1;
		while (A < B) {
			if (B % 2 == 0) {
				ans++;
				B = B / 2;
				continue;
			}
			if (B % 10 == 1) {
				ans++;
				B = B / 10;
				continue;
			}
			break;
		}
		if (A == B) {
			System.out.println(ans);
		} else
			System.out.println(-1);
	}
}
