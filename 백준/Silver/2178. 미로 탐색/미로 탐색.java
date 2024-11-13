import java.util.Arrays;
import java.util.Scanner;

public class Main {
	private static int[][] visited;
	private static int[][] field;
	private static int N;
	private static int M;
	private static int ans;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		field = new int[N][M];
		visited = new int[N][M];
		ans = N * M;
		for (int i = 0; i < N; i++) {
			field[i] = Arrays.stream(sc.next().split("")).mapToInt(Integer::parseInt).toArray();
			Arrays.fill(visited[i], N * M);
		}
		dfs(0, 0, 1);
		System.out.println(ans);
	}

	private static void dfs(int x, int y, int k) {
		if (x == N - 1 && y == M - 1) {
			ans = Math.min(ans, k);
		}
		visited[x][y] = k;
		int binaryCheck = check(x, y);
		if (binaryCheck % 2 == 1) {
			if (visited[x][y + 1] > k + 1) {
				dfs(x, y + 1, k + 1);
			}
		}
		binaryCheck /= 2;
		if (binaryCheck % 2 == 1) {
			if (visited[x][y - 1] > k + 1) {
				dfs(x, y - 1, k + 1);
			}
		}
		binaryCheck /= 2;
		if (binaryCheck % 2 == 1) {
			if (visited[x + 1][y] > k + 1) {
				dfs(x + 1, y, k + 1);
			}
		}
		binaryCheck /= 2;
		if (binaryCheck % 2 == 1) {
			if (visited[x - 1][y] > k + 1) {
				dfs(x - 1, y, k + 1);
			}
		}
	}

	// binaryCheck(상하좌우) 0000 : 상하좌우 다 visited || 0
	private static int check(int row, int col) {
		int ans = 0;
		if (row > 0 && field[row - 1][col] == 1) {
			ans |= 1 << 3;
		}
		if (row < field.length - 1 && field[row + 1][col] == 1) {
			ans |= 1 << 2;
		}
		if (col > 0 && field[row][col - 1] == 1) {
			ans |= 1 << 1;
		}
		if (col < field[0].length - 1 && field[row][col + 1] == 1) {
			ans |= 1;
		}
		return ans;
	}

}
