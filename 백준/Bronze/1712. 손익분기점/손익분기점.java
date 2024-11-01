import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int C = sc.nextInt();
		int profit = C - B;
		if (profit <= 0) {
			System.out.println(-1);
			System.exit(0);
		}
		System.out.println(A / profit + 1);
	}
}
