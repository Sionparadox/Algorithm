import java.util.HashMap;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		HashMap<String, Integer> names = new HashMap<>();
		int N = sc.nextInt();
		for (int i = 0; i < N; i++) {
			String name = sc.next();
			names.put(name, names.getOrDefault(name, 0) + 1);
		}
		for (int i = 0; i < N - 1; i++) {
			String name = sc.next();
			names.put(name, names.get(name) - 1);
		}
		for (String name : names.keySet()) {
			if (names.get(name) != 0)
				System.out.println(name);
		}
	}
}
