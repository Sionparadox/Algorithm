import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String binary = sc.next();
		int toZero = 0;
		int toOne = 0;
		boolean zeroFlag = false;
		boolean oneFlag = false;
		for (int i = 0; i < binary.length(); i++) {
			if (binary.charAt(i) == '0' && !zeroFlag) {
				toZero++;
				zeroFlag = true;
				oneFlag = false;
			} else if (binary.charAt(i) == '1' && !oneFlag) {
				toOne++;
				oneFlag = true;
				zeroFlag = false;
			}

		}
		System.out.println(Math.min(toZero, toOne));
	}
}
