import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] arr = new int[n][2];
		for (int i = 0; i < n; i++) {
			arr[i][0] = sc.nextInt();
			arr[i][1] = sc.nextInt();
		}
		Arrays.sort(arr, (a, b) -> {
			int result = Integer.compare(a[1], b[1]);
			if (result == 0) {
				result = Integer.compare(a[0], b[0]);
			}
			return result;
		});
		int end = 0;
		int ans = 0;
		for (int i = 0; i < n; i++) {
			if (arr[i][0] >= end) {
				ans++;
				end = arr[i][1];
			}
		}
		System.out.println(ans);
	}

}