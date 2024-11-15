import java.util.Scanner;

public class Main {
	private static boolean[] visited;
	private static boolean[][] graph;
	private static int N, ans = -1;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		int pairCnt = sc.nextInt();
		graph = new boolean[N + 1][N + 1];
		visited = new boolean[N + 1];
		for (int i = 0; i < pairCnt; i++) {
			int n1 = sc.nextInt();
			int n2 = sc.nextInt();
			graph[n1][n2] = true;
			graph[n2][n1] = true;
		}
		dfs(1);
		System.out.println(ans);
	}

	private static void dfs(int virus) {
		visited[virus] = true;
		ans++;
		for (int i = 1; i <= N; i++) {
			if (graph[virus][i] && !visited[i]) {
				dfs(i);
			}
		}

	}
}
