import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int[][] field;
	static int N, K;
	static int[][] visited;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		K = sc.nextInt();
		field = new int[2][N];
		visited = new int[2][N];
		for (int i = 0; i < 2; i++) {
			String nums = sc.next();
			for (int j = 0; j < N; j++) {
				field[i][j] = nums.charAt(j) - '0';
				visited[i][j] = 100000;
			}
		}

		if (bfs()) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
	}

	public static boolean bfs() {
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(new int[] {0, 0});
		visited[0][0] = 0;

		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int line = cur[0];
			int pos = cur[1];
			int time = visited[line][pos];
			if (pos + K >= N) {
				return true;
			}

			if (pos + 1 < N && visited[line][pos + 1] > time + 1 && field[line][pos + 1] == 1) {
				queue.offer(new int[] {line, pos + 1});
				visited[line][pos + 1] = time + 1;
			}
			if (pos - 1 > time && visited[line][pos - 1] > time + 1 && field[line][pos - 1] == 1) {
				queue.offer(new int[] {line, pos - 1});
				visited[line][pos - 1] = time + 1;
			}
			if (pos + K < N && visited[1 - line][pos + K] > time + 1 && field[1 - line][pos + K] == 1) {
				queue.offer(new int[] {1 - line, pos + K});
				visited[1 - line][pos + K] = time + 1;
			}
		}
		return false;
	}
}
