import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] parents;
	static int[] size;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		parents = new int[1000001];
		size = new int[1000001];

		for (int i = 0; i < 1000001; i++) {
			parents[i] = i;
			size[i] = 1;
		}

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			char order = st.nextToken().charAt(0);
			if (order == 'I') {
				int part1 = Integer.parseInt(st.nextToken());
				int part2 = Integer.parseInt(st.nextToken());
				union(part1, part2);
			} else {
				int c = Integer.parseInt(st.nextToken());
				System.out.println(size[find(c)]);
			}
		}
	}

	public static int find(int x) {
		if (parents[x] == x) {
			return x;
		}
		return parents[x] = find(parents[x]);
	}

	public static void union(int x, int y) {
		int rootX = find(x);
		int rootY = find(y);
		if (rootX != rootY) {
			parents[rootY] = rootX;
			size[rootX] += size[rootY];
		}
	}
}
