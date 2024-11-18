import java.util.Scanner;

public class Main {
	private static char[][] field;
	private static boolean[][] visited;
	private static int N;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		field = new char[N][N];
		visited = new boolean[N][N];
		for (int i = 0; i < N; i++) {
			field[i] = sc.next().toCharArray();
		}
		int ans = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					dfs(i, j, field[i][j], false);
					ans++;
				}
			}
		}
		System.out.print(ans + " ");
		visited = new boolean[N][N];
		ans = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					dfs(i, j, field[i][j], true);
					ans++;
				}
			}
		}
		System.out.println(ans);
	}

	private static void dfs(int x, int y, char c, boolean rb) {
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		visited[x][y] = true;

		for (int d = 0; d < 4; d++) {
			int nx = x + dx[d];
			int ny = y + dy[d];
			if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
				if (!rb && field[nx][ny] == c) {
					dfs(nx, ny, c, rb);
				} else if (rb) {
					if ((c == 'R' || c == 'G') && (field[nx][ny] == 'R' || field[nx][ny] == 'G')) {
						dfs(nx, ny, c, rb);
					} else if (field[nx][ny] == c) {
						dfs(nx, ny, c, rb);
					}
				}
			}
		}

	}
}
