import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	private static int[][] field;
	private static int N, M;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		field = new int[N][M];
		for (int i = 0; i < N; i++) {
			field[i] = Arrays.stream(sc.next().split("")).mapToInt(Integer::parseInt).toArray();
		}

		int ans = bfs(0, 0);
		System.out.println(ans);
	}

	private static int bfs(int x, int y) {
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		int[][][] visited = new int[N][M][2];
		for (int[][] row : visited) {
			for (int[] col : row) {
				Arrays.fill(col, -1);
			}
		}
		visited[x][y][0] = 1;
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(new int[] {x, y, 0});

		while (!queue.isEmpty()) {
			int[] pos = queue.poll();
			int px = pos[0], py = pos[1], breakCnt = pos[2];
			if (pos[0] == N - 1 && pos[1] == M - 1) {
				return visited[px][py][breakCnt];
			}

			for (int i = 0; i < 4; i++) {
				int nx = px + dx[i];
				int ny = py + dy[i];
				if (nx >= 0 && nx < N && ny >= 0 && ny < M) {
					if (field[nx][ny] == 0 && visited[nx][ny][breakCnt] == -1) {
						visited[nx][ny][breakCnt] = visited[px][py][breakCnt] + 1;
						queue.offer(new int[] {nx, ny, breakCnt});
					}
					if (field[nx][ny] == 1 && breakCnt == 0 && visited[nx][ny][1] == -1) {
						visited[nx][ny][1] = visited[px][py][0] + 1;
						queue.offer(new int[] {nx, ny, 1});
					}
				}

			}
		}
		return -1;
	}
}
