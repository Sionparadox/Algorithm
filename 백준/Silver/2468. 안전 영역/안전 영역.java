import java.util.Scanner;

public class Main {
	private static int N, ans;
	private static boolean[][] notSink, visited;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		int[][] field = new int[N][N];
		int min = N;
		int max = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				field[i][j] = sc.nextInt();
				min = Math.min(min, field[i][j]);
				max = Math.max(max, field[i][j]);
			}
		}
		int ans = 0;

		for (int h = min; h <= max; h++) {
			notSink = new boolean[N][N];
			visited = new boolean[N][N];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					notSink[i][j] = field[i][j] > h;
				}
			}
			int cnt = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (notSink[i][j] && !visited[i][j]) {
						dfs(i, j);
						cnt++;
					}
				}
			}
			ans = Math.max(ans, cnt);
		}
        if (ans == 0)
			ans = 1;
		System.out.println(ans);
	}

	private static void dfs(int x, int y) {
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		visited[x][y] = true;
		for (int d = 0; d < 4; d++) {
			int nx = x + dx[d];
			int ny = y + dy[d];
			if (nx >= 0 && nx < N && ny >= 0 && ny < N && notSink[nx][ny] && !visited[nx][ny]) {
				dfs(nx, ny);
			}
		}

	}
}
