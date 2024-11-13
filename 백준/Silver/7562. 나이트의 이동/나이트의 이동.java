import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	private static int N, endX, endY;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int t = 0; t < T; t++) {
			N = sc.nextInt();
			int startX = sc.nextInt();
			int startY = sc.nextInt();
			endX = sc.nextInt();
			endY = sc.nextInt();
			int ans = bfs(startX, startY);
			System.out.println(ans);
		}
	}

	private static int bfs(int x, int y) {
		int[] dx = {-2, -2, -1, -1, 1, 1, 2, 2};
		int[] dy = {-1, 1, -2, 2, -2, 2, -1, 1};
		int[][] visited = new int[N][N];
		visited[x][y] = 1;
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(new int[] {x, y});
		while (!queue.isEmpty()) {
			int[] pos = queue.poll();
			if (pos[0] == endX && pos[1] == endY) {
				return visited[pos[0]][pos[1]] - 1;
			}
			for (int i = 0; i < 8; i++) {
				int nx = pos[0] + dx[i];
				int ny = pos[1] + dy[i];
				if (nx >= 0 && nx < N && ny >= 0 && ny < N && visited[nx][ny] == 0) {
					visited[nx][ny] = visited[pos[0]][pos[1]] + 1;
					queue.offer(new int[] {nx, ny});
				}
			}
		}

		return 0;
	}

}
