import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		for (int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		Arrays.sort(arr);
		int maxWeight = 0;
		for (int i = 0; i < n; i++) {
			maxWeight = Math.max(maxWeight, arr[i] * (arr.length - i));
		}
		System.out.println(maxWeight);
	}
}
