import java.util.Scanner;

public class Main {
	static int[][] field;
	static int N;
	static int M;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		int R = sc.nextInt();
		field = new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				field[i][j] = sc.nextInt();
			}
		}
		for (int i = 0; i < R; i++) {
			rotate();
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				System.out.print(field[i][j] + " ");
			}
			System.out.println();
		}
	}

	//한번 이동(반시계)
	public static void rotate() {
		int step = Math.min(N, M);
		int[][] rotated = new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				int depth = calcDepth(i, j);
				if (i == depth) {
					if (j == depth) {
						rotated[i + 1][j] = field[i][j];
					} else {
						rotated[i][j - 1] = field[i][j];
					}
				} else if (i == N - depth - 1) {
					if (j == M - depth - 1) {
						rotated[i - 1][j] = field[i][j];
					} else {
						rotated[i][j + 1] = field[i][j];
					}
				} else if (j == depth) {
					rotated[i + 1][j] = field[i][j];
				} else if (j == M - depth - 1) {
					rotated[i - 1][j] = field[i][j];
				}
			}
		}
		field = rotated;
	}

	public static int calcDepth(int n, int m) {
		return Math.min(Math.min(n, N - n - 1), Math.min(m, M - m - 1));
	}
}
