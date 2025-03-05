import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static char[][] field;
	static boolean[][] visited;
	static int R, C;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		R = sc.nextInt();
		C = sc.nextInt();
		field = new char[R][C];
		visited = new boolean[R][C];
		for (int i = 0; i < R; i++) {
			String temp = sc.next();
			for (int j = 0; j < temp.length(); j++) {
				field[i][j] = temp.charAt(j);
				if (temp.charAt(j) == '#') {
					visited[i][j] = true;
				}
			}
		}
		int[][] move;
		move = new int[][] {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
		Queue<int[]> queue = new LinkedList<>();
		int[] res = new int[] {0, 0};
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (!visited[i][j]) {
					int[] temp = new int[] {0, 0};
					queue.add(new int[] {i, j});
					visited[i][j] = true;
					while (!queue.isEmpty()) {
						int[] poll = queue.poll();
						int x = poll[0], y = poll[1];
						if (field[x][y] == 'o') {
							temp[0] += 1;
						} else if (field[x][y] == 'v') {
							temp[1] += 1;
						}
						for (int[] d : move) {
							int dx = x + d[0];
							int dy = y + d[1];
							if (dx >= 0 && dx < R && dy >= 0 && dy < C) {
								if (!visited[dx][dy] && field[dx][dy] != '#') {
									queue.add(new int[] {dx, dy});
									visited[dx][dy] = true;
								}
							}
						}
					}
					if (temp[1] == Arrays.stream(temp).max().getAsInt()) {
						res[1] += temp[1];
					} else {
						res[0] += temp[0];
					}
				}
			}
		}
		System.out.println(res[0] + " " + res[1]);
	}
}
