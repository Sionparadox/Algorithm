import java.util.HashMap;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String nickname = sc.next();
		HashMap<Character, Integer> map = new HashMap<>();
		for (char c : nickname.toCharArray()) {
			map.put(c, map.getOrDefault(c, 0) + 1);
		}
		String center = "";
		for (char k : map.keySet()) {
			if (map.get(k) % 2 == 1) {
				if (center.equals("")) {
					map.put(k, map.get(k) - 1);
					center = k + "";
				} else {
					System.out.println("I'm Sorry Hansoo");
					return;
				}
			}
		}
		StringBuilder side = new StringBuilder();
		for (char c = 'A'; c <= 'Z'; c++) {
			if (map.containsKey(c)) {
				side.append((c + "").repeat(map.get(c) / 2));
			}
		}
		System.out.println(side.toString() + center + side.reverse().toString());
	}
}
