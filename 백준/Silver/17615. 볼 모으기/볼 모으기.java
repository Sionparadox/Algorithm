import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		String balls = sc.next();
		ArrayList<Integer> ballLen = new ArrayList<>();
		ballLen.add(0);
		char prev = balls.charAt(0);
		for (char b : balls.toCharArray()) {
			if (b == prev) {
				ballLen.set(ballLen.size() - 1, ballLen.get(ballLen.size() - 1) + 1);
			} else {
				prev = b;
				ballLen.add(1);
			}
		}
		if (ballLen.size() <= 2) {
			System.out.println(0);
			return;
		}
		int oddSum = 0;
		int evenSum = 0;
		for (int i = 1; i < ballLen.size() - 1; i++) {
			if (i % 2 == 0) {
				oddSum += ballLen.get(i);
			} else {
				evenSum += ballLen.get(i);
			}
		}
		oddSum += ballLen.size() % 2 == 0 ? 0 : Math.min(ballLen.get(0), ballLen.get(ballLen.size() - 1));
		System.out.println(Math.min(evenSum, oddSum));
	}
}
