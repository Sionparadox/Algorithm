import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int K = sc.nextInt();
		Queue<int[]> queue = new PriorityQueue<>((a, b) -> {
			if (a[0] == b[0]) {
				return b[1] - a[1];
			}
			return a[0] - b[0];
		});

		for (int i = 0; i < N; i++) {
			queue.offer(new int[] {sc.nextInt(), sc.nextInt()});
		}
		for (int i = 0; i < K; i++) {
			queue.offer(new int[] {sc.nextInt(), -1});
		}
		Queue<int[]> jewel = new PriorityQueue<>((a, b) -> b[1] - a[1]);
		long ans = 0;
		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			if (cur[1] == -1) {
				if (!jewel.isEmpty()) {
					ans += jewel.poll()[1];
				}
			} else {
				jewel.offer(cur);
			}
		}
		System.out.println(ans);
	}
}
