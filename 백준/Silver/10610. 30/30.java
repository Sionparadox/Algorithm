import java.util.Arrays;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String[] number = sc.next().split("");
		boolean hasZero = false;
		int sumNumber = 0;
		Integer[] nums = new Integer[number.length];
		for (int i = 0; i < number.length; i++) {
			if (number[i].equals("0")) {
				hasZero = true;
			}
			nums[i] = Integer.parseInt(number[i]);
			sumNumber += nums[i];
		}
		if (hasZero && sumNumber % 3 == 0) {
			Arrays.sort(nums, (a, b) -> b - a);
			for (int i = 0; i < nums.length; i++) {
				System.out.print(nums[i]);
			}
			System.out.println();
		} else {
			System.out.println(-1);
		}

	}
}
