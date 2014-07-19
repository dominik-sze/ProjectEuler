import java.lang.Math.*;
import java.util.*;

public class Problem3 {
	public static void main(String[] args) {
		Problem3 p3 = new Problem3();
		p3.problem3();
	}

	public void problem3() {
		long number = 600851475143L;
		//long number = 13195L;
		for(long i=(int)Math.sqrt(number); i>2; i--) {
			if(number%i==0 && isPrime(i)) {
				System.out.println(i);
				return;
			}
		}
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
