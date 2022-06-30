/*
Largest prime factor

Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

import java.math.BigInteger;

public class P003_largestPrimeFactor {
    public static int largestPrimeFactor(BigInteger target) {
        int result = 0;
        for (int i=2; BigInteger.valueOf(i).compareTo(target.sqrt()) == -1; i++) {
            if (target.remainder(BigInteger.valueOf(i)) == BigInteger.ZERO && i>result) {
                result = i;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        BigInteger target = new BigInteger("600851475143");
        int result = largestPrimeFactor(target);
        System.out.println("The target is " + target);
        System.out.println("The largest prime factor is " + result);
    }
}