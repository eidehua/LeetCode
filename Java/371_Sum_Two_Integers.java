/*
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

(Python has some issues with this simple code on negative number cases, I think because when overflow happens, the variables for a and b overflow from int to long, I have to look into it)
*/
public class Solution {
	public int getSum(int a, int b) {
		if (a == 0) return b;
		if (b == 0) return a;

		while (b != 0) {
			int carry = a & b;
			//System.out.println(carry);
			// for negative number, the carry will eventually overflow
			a = a ^ b;
			b = carry << 1;
		}
		
		return a;
	}
}