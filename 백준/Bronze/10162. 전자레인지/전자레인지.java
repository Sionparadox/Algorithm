import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int time = sc.nextInt();
		int A = time / 300;
		time %= 300;
		int B = time / 60;
		time %= 60;
		int C = time / 10;
		time %= 10;
		if (time != 0)
			System.out.println(-1);
		else {
			System.out.printf("%d %d %d\n", A, B, C);
		}
		sc.close();
	}
}
