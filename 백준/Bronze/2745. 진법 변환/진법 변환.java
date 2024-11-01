import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String rawNum = sc.next();
		int B = sc.nextInt();
		int ans = Integer.parseInt(rawNum, B);
		System.out.println(ans);
	}
}
