import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		Queue<Integer> queue = new PriorityQueue<>();
		for (int i = 0; i < N; i++) {
			queue.add(sc.nextInt());
		}
		int ans = 0;

		while (queue.size() > 1) {
			int a = queue.poll();
			int b = queue.poll();
			int sum = a + b;
			ans += sum;
			queue.add(sum);
		}
		System.out.println(ans);
	}
}