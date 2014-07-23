import java.math.*;

public class Problem16 {
	public static void main(String[] args) {
		problem16();
	}

	private static void problem16() {
		BigInteger number = new BigInteger("2");
		number = number.pow(1000);
		BigInteger ten = new BigInteger("10");
		BigInteger zero = new BigInteger("0");
		int result = 0;
		while(number.compareTo(zero)>0) {
			result += number.mod(ten).intValue();
			number = number.divide(ten);
		}
		System.out.println(result);
	}
}
