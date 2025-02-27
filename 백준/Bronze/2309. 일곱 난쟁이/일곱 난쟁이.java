import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] dwarfs = new int[9];
		for (int i = 0; i < 9; i++) {
			dwarfs[i] = sc.nextInt();
		}
		int limit = Arrays.stream(dwarfs).sum() - 100;
		Arrays.sort(dwarfs);
		int i = 8;
		int j = 8;
		for (i = 8; i > -1; i--) {
			if (dwarfs[i] > limit) {
				continue;
			}
			int newLimit = limit - dwarfs[i];
			for (j = i - 1; j > -1; j--) {
				if (dwarfs[j] == newLimit) {
					break;
				}
			}
			if (j != -1) {
				break;
			}
		}
		for (int k = 0; k < 9; k++) {
			if (k != i && k != j) {
				System.out.println(dwarfs[k]);
			}
		}

	}
}
