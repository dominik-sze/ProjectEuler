import java.util.*;

public class Problem4 {
	public static void main(String[] args) {
		Problem4 p4 = new Problem4();
		p4.solution();
	}

	public void solution() {
		ArrayList<Integer> res = new ArrayList<Integer>();
		String val = null;
		for(int i=999; i>99; i--) {
			for(int j=999; j>99; j--) {
				val = Integer.toString(i*j);
				if(val.substring(0, val.length()/2).equals((new StringBuilder(val.substring(val.length()/2, val.length())).reverse().toString()))) {
					res.add(Integer.valueOf(val));
				}
			}
		}
		Collections.sort(res);
		System.out.println(res.get(res.size()-1));
	}
}
