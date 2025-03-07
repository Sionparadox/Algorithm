import java.util.Scanner;

public class Main {
	static int N, M;
	static int[][] field;

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
			int order = sc.nextInt();
			switch (order) {
				case 1:
					reverseRow();
					break;
				case 2:
					reverseCol();
					break;
				case 3:
					rotateRight();
					break;
				case 4:
					rotateLeft();
					break;
				case 5:
					partitionRight();
					break;
				case 6:
					partitionLeft();
					break;
			}
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				System.out.print(field[i][j] + " ");
			}
			System.out.println();
		}
	}

	static void reverseRow() {
		for (int i = 0; i < N / 2; i++) {
			int[] temp = field[i];
			field[i] = field[N - 1 - i];
			field[N - i - 1] = temp;
		}
	}

	static void reverseCol() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M / 2; j++) {
				int temp = field[i][j];
				field[i][j] = field[i][M - j - 1];
				field[i][M - j - 1] = temp;
			}
		}
	}

	static void rotateRight() {
		int[][] temp = new int[M][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				temp[j][N - i - 1] = field[i][j];
			}
		}
		field = temp;
		int t = N;
		N = M;
		M = t;
	}

	static void rotateLeft() {
		int[][] temp = new int[M][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				temp[M - j - 1][i] = field[i][j];
			}
		}
		field = temp;
		int t = N;
		N = M;
		M = t;
	}

	static void partitionRight() {
		int[][] temp = new int[N][M];
		for (int i = 0; i < N / 2; i++) {
			for (int j = 0; j < M / 2; j++) {
				temp[i][j + M / 2] = field[i][j];
			}
		}
		for (int i = 0; i < N / 2; i++) {
			for (int j = M / 2; j < M; j++) {
				temp[i + N / 2][j] = field[i][j];
			}
		}
		for (int i = N / 2; i < N; i++) {
			for (int j = M / 2; j < M; j++) {
				temp[i][j - M / 2] = field[i][j];
			}
		}
		for (int i = N / 2; i < N; i++) {
			for (int j = 0; j < M / 2; j++) {
				temp[i - N / 2][j] = field[i][j];
			}
		}
		field = temp;
	}

	static void partitionLeft() {
		int[][] temp = new int[N][M];
		for (int i = 0; i < N / 2; i++) {
			for (int j = 0; j < M / 2; j++) {
				temp[i + N / 2][j] = field[i][j];
			}
		}
		for (int i = 0; i < N / 2; i++) {
			for (int j = M / 2; j < M; j++) {
				temp[i][j - M / 2] = field[i][j];
			}
		}
		for (int i = N / 2; i < N; i++) {
			for (int j = M / 2; j < M; j++) {
				temp[i - N / 2][j] = field[i][j];
			}
		}
		for (int i = N / 2; i < N; i++) {
			for (int j = 0; j < M / 2; j++) {
				temp[i][j + M / 2] = field[i][j];
			}
		}
		field = temp;
	}
}
