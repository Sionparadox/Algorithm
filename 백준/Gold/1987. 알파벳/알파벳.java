import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
	private static char[][] field;
	private static int R, C, ans;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		R = sc.nextInt();
		C = sc.nextInt();
		field = new char[R][C];
		Map<Character, Integer> visitCnt = new HashMap<>();
		for (int i = 0; i < R; i++) {
			field[i] = sc.next().toCharArray();
		}
		visitCnt.put(field[0][0], 1);
		dfs(0, 0, visitCnt);
		System.out.println(ans);
	}

	private static void dfs(int x, int y, Map<Character, Integer> map) {
		ans = Math.max(ans, map.get(field[x][y]));
		if (x == R - 1 && y == C - 1) {
			return;
		}
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		for (int d = 0; d < 4; d++) {
			int nx = x + dx[d];
			int ny = y + dy[d];
			if (nx >= 0 && nx < R && ny >= 0 && ny < C) {
				if (map.containsKey(field[nx][ny])) {
					continue;
				}
				map.put(field[nx][ny], map.get(field[x][y]) + 1);
				dfs(nx, ny, map);
				map.remove(field[nx][ny]);
			}
		}
	}
}
