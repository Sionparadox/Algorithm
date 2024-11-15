import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
	private static boolean[] visited;
	private static List<Integer>[] graph;
	private static int[] ans;
	private static int N;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		visited = new boolean[N + 1];
		ans = new int[N + 1];
		graph = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			graph[i] = new ArrayList<>();
		}
		for (int i = 1; i < N; i++) {
			int n1 = sc.nextInt();
			int n2 = sc.nextInt();
			graph[n1].add(n2);
			graph[n2].add(n1);
		}
		dfs(1);
		for (int i = 2; i <= N; i++) {
			System.out.println(ans[i]);
		}
	}

	private static void dfs(int node) {
		visited[node] = true;
		for (int i : graph[node]) {
			if (!visited[i]) {
				ans[i] = node;
				dfs(i);
			}
		}
	}
}
