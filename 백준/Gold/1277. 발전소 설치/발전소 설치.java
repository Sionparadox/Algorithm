import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int W = sc.nextInt();
		double limit = sc.nextDouble();
		int[][] powers = new int[N][2];
		double[][] distances = new double[N][N]; //dp[i][j] i번째에서 j번째 발전소까지 최소거리
		for (int i = 0; i < N; i++) {
			powers[i][0] = sc.nextInt();
			powers[i][1] = sc.nextInt();
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				double distance = Math.sqrt(
					Math.pow(powers[i][0] - powers[j][0], 2) + Math.pow(powers[i][1] - powers[j][1], 2));
				distances[i][j] = distance <= limit ? distance : Double.POSITIVE_INFINITY;
			}
		}
		for (int i = 0; i < W; i++) {
			int node1 = sc.nextInt() - 1;
			int node2 = sc.nextInt() - 1;
			distances[node1][node2] = 0;
			distances[node2][node1] = 0;
		}

		double[] dp = new double[N];
		boolean[] visited = new boolean[N];
		Arrays.fill(dp, Double.POSITIVE_INFINITY);
		dp[0] = 0;
		for (int i = 0; i < N; i++) {
			int current = -1;
			double minDist = Double.POSITIVE_INFINITY;
			for (int j = 0; j < N; j++) {
				if (!visited[j] && dp[j] < minDist) {
					current = j;
					minDist = dp[j];
				}
			}

			if (current == -1) {
				break;
			}
			visited[current] = true;

			for (int j = 0; j < N; j++) {
				if (!visited[j] && distances[current][j] != Double.POSITIVE_INFINITY) {
					dp[j] = Math.min(dp[j],
						dp[current] + distances[current][j]);
				}
			}
		}
		System.out.println((int)(dp[N - 1] * 1000));

	}
}
