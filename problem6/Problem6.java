public class Problem6 {
	public static void main(String[] args) {
		Problem6 p6 = new Problem6();
		p6.solution();
	}

	public void solution() {
		int sumSqrt = 0;
		int sqrtSum = 0;
		for(int i=1; i<=100; i++) {
			sumSqrt += i*i;
			sqrtSum += i;
		}
		System.out.println(sqrtSum*sqrtSum-sumSqrt);
	}
}
		

