public class Problem7 {
	public static void main(String[] args) {
		Problem7 p7 = new Problem7();
		p7.solution();
	}

	public void solution() {
		int counter = 0;
		int num = 0; 
		while(counter<10001) {
			num++;
			if(isPrime(num)) {
				counter++;
			}
		}
		System.out.println(num);
	}

	private boolean isPrime(long num) {
		if(num<=3) {
			if(num<=1) {
				return false;
			}
			return true;
		}
		if(num%2==0 || num%3==0) {
			return false;
		}
		for(long i=5; i<(long)(Math.pow(num,0.5)+1); i+=6) {
			if(num%i==0 || (num%(i+2))==0) {
				return false;
			}
		}
		return true;
	}
}
