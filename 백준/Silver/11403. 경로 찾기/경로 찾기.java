import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	private static ArrayList<ArrayList<Integer>> graph;
	private static int N;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();

		graph = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			graph.add(new ArrayList<>());
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				graph.get(i).add(sc.nextInt());
			}
		}

		for (int i = 0; i < N; i++) {
			bfs(i);
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				System.out.print(graph.get(i).get(j) + " ");
			}
			System.out.println();
		}
	}

	private static void bfs(int node) {
		boolean[] visited = new boolean[N];
		Queue<Integer> queue = new LinkedList<>();
		queue.add(node);
		while (!queue.isEmpty()) {
			int poll = queue.poll();
			for (int i = 0; i < N; i++) {
				if (graph.get(poll).get(i) == 1 && !visited[i]) {
					visited[i] = true;
					queue.offer(i);
					graph.get(node).set(i, 1);
				}
			}

		}
	}
}
