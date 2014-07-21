public class Problem5 {
	public static void main(String[] args) {
		Problem5 p5 = new Problem5();
		p5.solution();
	}

	public void solution() {
		int num = 2520;
		while(true) {
			int i;
			for(i=20; i>0; i--) {
				if(num%i!=0) {
					break;
				}
			}
			if(i==0) {
				System.out.println(num);
				break;
			}
			num+=10;
		}
	}
}
