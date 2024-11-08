import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Queue<Integer> positive = new PriorityQueue<>((a, b) -> b - a);
		Queue<Integer> negative = new PriorityQueue<>((a, b) -> a - b);
		for (int i = 0; i < n; i++) {
			int sInt = sc.nextInt();
			if (sInt > 0) {
				positive.add(sInt);
			} else {
				negative.add(sInt);
			}
		}
		int ans = 0;
		int num = 0;
		while (!positive.isEmpty()) {
			if (num == 0) {
				num = positive.poll();
			} else {
				int temp = positive.poll();
				if (temp > 1) {
					ans += num * temp;
				} else {
					ans += temp + num;
				}
				num = 0;
			}
		}
		if (num != 0) {
			ans += num;
		}

		num = 1;
		while (!negative.isEmpty()) {
			if (num == 1) {
				num = negative.poll();
			} else {
				ans += num * negative.poll();
				num = 1;
			}
		}
		if (num != 1) {
			ans += num;
		}
		System.out.println(ans);
	}
}
