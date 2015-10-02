public class Solution {
	public int numDecodings(String s) {
		int n = s.length();
		if (n == 0 || s.startsWith("0")) {
			return 0;
		}
		int[] ways = new int[n+1];
		ways[0] = 1;
		ways[1] = 1;
		for (int i = 2; i <= n; i++) {
			int first = Integer.parseInt(s.substring(i-2, i));
			int prev = (first <= 26 && first > 9) ? ways[i-2]:0;
			int plus = (Integer.parseInt(s.substring(i-1, i)) == 0) ? 0:ways[i-1];
			ways[i] = prev + plus;
		}
		return ways[n];
	}
}
