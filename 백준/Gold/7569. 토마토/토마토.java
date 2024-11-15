import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	private static int N, M, H;
	private static int[][][] box;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		H = sc.nextInt();
		box = new int[H][M][N];
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < M; j++) {
				for (int k = 0; k < N; k++) {
					box[i][j][k] = sc.nextInt();
				}
			}
		}

		Queue<int[]> queue = new LinkedList<>();
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < M; j++) {
				for (int k = 0; k < N; k++) {
					if (box[i][j][k] == 1) {
						queue.offer(new int[] {i, j, k});
					}
				}
			}
		}

		bfs(queue);
		int ans = 0;
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < M; j++) {
				for (int k = 0; k < N; k++) {
					if (box[i][j][k] == 0) {
						System.out.println(-1);
						return;
					}
					ans = Math.max(ans, box[i][j][k]);
				}
			}
		}
		System.out.println(ans - 1);

	}

	private static void bfs(Queue<int[]> queue) {
		int[] dx = {-1, 1, 0, 0, 0, 0};
		int[] dy = {0, 0, -1, 1, 0, 0};
		int[] dz = {0, 0, 0, 0, -1, 1};

		while (!queue.isEmpty()) {
			int[] poll = queue.poll();
			int z = poll[0], y = poll[1], x = poll[2];
			for (int d = 0; d < 6; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				int nz = z + dz[d];
				if (nx >= 0 && nx < N && ny >= 0 && ny < M && nz >= 0 && nz < H) {
					if (box[nz][ny][nx] == 0) {
						queue.offer(new int[] {nz, ny, nx});
						box[nz][ny][nx] = box[z][y][x] + 1;
					}
				}
			}
		}
	}
}
