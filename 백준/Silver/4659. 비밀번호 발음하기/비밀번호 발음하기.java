import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
	static HashSet<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		while (true) {
			String pwd = sc.next();
			if (pwd.equals("end")) {
				break;
			}
			System.out.println("<" + pwd + "> is " + (checkPassword(pwd) ? "" : "not ") + "acceptable.");
		}
	}

	public static boolean checkPassword(String password) {
		boolean vowelFlag = false;
		for (int i = 0; i < password.length(); i++) {
			char c = password.charAt(i);
			if (i < password.length() - 1 && password.charAt(i + 1) == c && c != 'e' && c != 'o') {
				return false;
			}
			if (i < password.length() - 2 && (vowels.contains(c) == vowels.contains(
				password.charAt(i + 1))) && (vowels.contains(c) == vowels.contains(password.charAt(i + 2)))) {
				return false;
			}
			if (vowels.contains(c)) {
				vowelFlag = true;
			}
		}
		return vowelFlag;
	}
}
