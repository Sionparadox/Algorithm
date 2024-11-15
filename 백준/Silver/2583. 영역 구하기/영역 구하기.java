import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	private static boolean[][] field, visited;
	private static int N, M;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		M = sc.nextInt();
		N = sc.nextInt();
		int K = sc.nextInt();
		field = new boolean[M][N];
		visited = new boolean[M][N];
		for (int t = 0; t < K; t++) {
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();
			for (int i = y1; i < y2; i++) {
				for (int j = x1; j < x2; j++) {
					field[i][j] = true;
				}
			}
		}
		ArrayList<Integer> ans = new ArrayList<>();
		for (int i = 0; i < M; i++) {
			for (int j = 0; j < N; j++) {
				if (!field[i][j] && !visited[i][j]) {
					int temp = dfs(i, j);
					ans.add(temp);
				}
			}
		}
		System.out.println(ans.size());
		ans.sort(Integer::compareTo);
		for (int a : ans) {
			System.out.print(a + " ");
		}
		System.out.println();
	}

	private static int dfs(int y, int x) {
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		visited[y][x] = true;
		int res = 1;

		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >= 0 && nx < N && ny >= 0 && ny < M && !field[ny][nx] && !visited[ny][nx]) {
				res += dfs(ny, nx);
			}
		}
		return res;
	}
}
