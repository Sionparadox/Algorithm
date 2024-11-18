import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
	private static boolean[][] visited;
	private static int[][] field;
	private static int N, cnt;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		field = new int[N][N];
		visited = new boolean[N][N];
		ArrayList<Integer> ans = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			field[i] = Arrays.stream(sc.next().split("")).mapToInt(Integer::parseInt).toArray();
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j] && field[i][j] == 1) {
					cnt = 0;
					dfs(i, j);
					ans.add(cnt);
				}
			}
		}
		System.out.println(ans.size());
		Collections.sort(ans);
		for (var a : ans) {
			System.out.println(a);
		}
	}

	private static void dfs(int x, int y) {
		visited[x][y] = true;
		cnt++;
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		for (int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny] && field[nx][ny] == 1) {
				dfs(nx, ny);
			}
		}
	}
}
