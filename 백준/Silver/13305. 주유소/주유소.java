import java.math.BigInteger;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int[] distances = new int[N - 1];
		int[] oilPrices = new int[N];
		for (int i = 0; i < N - 1; i++) {
			distances[i] = sc.nextInt();
		}
		for (int i = 0; i < N; i++) {
			oilPrices[i] = sc.nextInt();
		}
		for (int i = 0; i < N - 1; i++) {
			if (oilPrices[i] < oilPrices[i + 1]) {
				oilPrices[i + 1] = oilPrices[i];
			}
		}
		BigInteger ans = BigInteger.ZERO;
		for (int i = 0; i < N - 1; i++) {
			ans = ans.add(BigInteger.valueOf(distances[i]).multiply(BigInteger.valueOf(oilPrices[i])));
		}
		System.out.println(ans);
	}

}
