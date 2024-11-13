import java.util.Scanner;

public class Main {
	private static int[][] field;
	private static boolean[][] visited;
	private static int N, M;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			M = sc.nextInt();
			N = sc.nextInt();
			if (N == 0 && M == 0)
				break;
			field = new int[N][M];
			visited = new boolean[N][M];
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					field[i][j] = sc.nextInt();
				}
			}
			int ans = 0;
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					if (!visited[i][j] && field[i][j] == 1) {
						dfs(i, j);
						ans++;
					}
				}
			}
			System.out.println(ans);
		}

	}

	private static void dfs(int x, int y) {
		int[] dx = {-1, 0, 1};
		int[] dy = {-1, 0, 1};
		visited[x][y] = true;
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (i == 1 && j == 1) {
					continue;
				}
				int nx = x + dx[i];
				int ny = y + dy[j];
				if (nx >= 0 && nx < N && ny >= 0 && ny < M && !visited[nx][ny] && field[nx][ny] == 1) {
					dfs(nx, ny);
				}
			}
		}
	}

}
