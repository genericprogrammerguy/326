/* File: CountingApp.java - Jan 2020 */

import java.util.*;

/**
A basic computer program which takes an input of 64-bit integers computes the value of (f) for given n and k
 then outputs a 64-bit interger.
 **For example:**
 Output for the value of
 (n k) = (52 5) = 52! / 5!(52−5)! = 2598960
 */

//May be run with input from file, for example using java CountingApp < testfile.txt
public class CountingApp {
    /**
     * Runs the main program and takes input from [system.in] check for a number of exception
     *
     * @param args An array of strings which stores arguments passed by command line while starting a program.
     */
    public static void main( String[] args ) {
        CountingApp ca = new CountingApp();
        Scanner sc = new Scanner(System.in);
        String temp1 = "";
        System.err.println("Enter integers n and k to compute (n choose k):");
        while (sc.hasNext()) {
            long n = 0;
            long k = 0;
            boolean skip = false;
            String skipped = "";
            try {
                temp1 = sc.next();
                n = Long.parseUnsignedLong(temp1); //Note: this will not parse characters
            }
            catch (Exception e1) {
                if (ca.isAllDigit(temp1)) {
                    System.err.println("Input is larger than (2^64)-1. Please enter smaller input.");
                }
                else {
                    System.err.println("Invalid input - must be an integer");
                }
                skip = true;
            }
            if (skip) {
                skipped = sc.next();
            }
            else {
                try {
                    temp1 = sc.next();
                    k = Long.parseUnsignedLong(temp1); //Note: this will not parse characters
                }
                catch (Exception e2) {
                    if (ca.isAllDigit(temp1)) {
                        System.err.println("Input is larger than (2^64)-1. Please enter smaller input.");
                    }
                    else {
                        System.err.println("Invalid input - must be an integer");
                    }
                    skip = true;
                }
            }
            if (skip) {
                skip = false;
            }
            else {
                System.out.println(Long.toUnsignedString(n) + " choose " + Long.toUnsignedString(k) + " = ");
                if (Long.compareUnsigned(n, k) < 0) {
                    System.out.println("impossible: n must be greater than k");
                }
                else {
                    try {
                        System.out.println(ca.calculate(n, k));
                    }
                    catch (Exception e3) {
                        System.err.println("error: result is greater than 64 bits - maximum result is (2^64)-1");
                    }

                }
            }
        }
    }
    /**
     * Takes 2 longs (n and k) and preforms the main calculation
     * returns a string representation of the argument as an unsigned decimal value. The unsigned quotient of dividing the
     * first argument by the second where each argument and the result is interpreted as an unsigned value. Then returns
     * the unsigned remainder from dividing the first argument by the second where each argument and the result is
     * interpreted as an unsigned value and then compares the  two long values numerically. Parses the string argument
     * as an unsigned decimal long and returns a string.
     *
     * @param n the value of n in the above formula
     * @param k the value of k in the above formula
     * @return the answer of the above equation
     */
    public String calculate( long n, long k ) {
        Map<Long, Integer> tally_factors = new HashMap<Long, Integer>(); //Long for factors (key), Integer for tally (value)
        if (k == n || k == 0) {
            return "1";
        }
        else if (k == 1 || k == n - 1) {
            return Long.toUnsignedString(n);
        }
        else if ((k == 2 || k == n - 2) && Long.divideUnsigned(n, 2) < (Long.divideUnsigned(1 + Long.MAX_VALUE * 2, (n - 1)))) {
            String answer = "";
            long result = 0;
            if (Long.remainderUnsigned(n, 2) == 0) {
                result = Long.divideUnsigned(n, 2);
                answer = multiplyLong(result, (n - 1));
            }
            else {
                result = Long.divideUnsigned(n - 1, 2);
                answer = multiplyLong(result, n);
            }
            return answer;
        }
        else if ((k >= 3 && k <= n - 3) && Long.parseUnsignedLong(multiplyLong((n / 6), (n - 1))) < (Long.divideUnsigned((1 + Long.MAX_VALUE * 2), (n - 2)))) {
            // might have to treat k == 1 and k == n-1 separately as well
            long result = Long.parseUnsignedLong("1");
            long temp1 = Long.parseUnsignedLong("0");
            long temp2 = Long.parseUnsignedLong("0");
            if (k <= n - k) { //then n choose k is given by multiplying n -> n-k+1 and dividing by k!
                for (long i = Long.parseUnsignedLong(Long.toUnsignedString(k)); i >= 0; i--) {
                    temp1 = n - i + 1;
                    temp2 = i;
                    //factorize n-k, putting factors into factors array and tally of each factor into same index, but in tally array
                    if (temp1 <= n) {
                        for (long j = Long.parseUnsignedLong(Long.toUnsignedString(2)); j <= Long.parseUnsignedLong(Long.toUnsignedString((n - i + 1) / 2)); j++) {
                            while (temp1 % j == 0) {
                                if (tally_factors.get(j) == null) {
                                    tally_factors.put(j, 1);
                                }
                                else {
                                    tally_factors.put(j, tally_factors.get(j) + 1);
                                }
                                temp1 = temp1 / j;
                            }
                        }
                        if (tally_factors.get(temp1) == null) {
                            tally_factors.put(temp1, 1);
                        }
                        else {
                            tally_factors.put(temp1, tally_factors.get(temp1) + 1);
                        }
                    }
                    //factorze k in the same way, but subtracting tally, rather than adding
                    for (long l = Long.parseUnsignedLong(Long.toUnsignedString(2)); l <= Long.parseUnsignedLong(Long.toUnsignedString(i / 2)); l++) {
                        while (temp2 % l == 0) {
                            if (tally_factors.get(l) == null) {
                                tally_factors.put(l, -1);
                            }
                            else {
                                tally_factors.put(l, tally_factors.get(l) - 1);
                            }
                            temp2 = temp2 / l;
                        }
                    }
                    if (tally_factors.get(temp2) == null) {
                        tally_factors.put(temp2, -1);
                    }
                    else {
                        tally_factors.put(temp2, tally_factors.get(temp2) - 1);
                    }
                }
            }
            else { //then n choose k is given by multiplying n -> k+1 and dividing by (n-k)!
                for (long i = Long.parseUnsignedLong(Long.toUnsignedString(n)); i >= Long.parseUnsignedLong(Long.toUnsignedString(k + 1)); i--) {
                    temp1 = i;
                    temp2 = i - k;
                    //factorize n-k, putting factors into factors array and tally of each factor into same index, but in tally array
                    for (long j = Long.parseUnsignedLong(Long.toUnsignedString(2)); j <= Long.parseUnsignedLong(Long.toUnsignedString(i / 2)); j++) {
                        while (temp1 % j == 0) {
                            if (tally_factors.get(j) == null) {
                                tally_factors.put(j, 1);
                            }
                            else {
                                tally_factors.put(j, tally_factors.get(j) + 1);
                            }
                            temp1 = temp1 / j;
                        }
                    }
                    if (tally_factors.get(temp1) == null) {
                        tally_factors.put(temp1, 1);
                    }
                    else {
                        tally_factors.put(temp1, tally_factors.get(temp1) + 1);
                    }
                    //factorze k in the same way, but subtracting tally, rather than adding
                    for (long l = Long.parseUnsignedLong(Long.toUnsignedString(2)); l <= Long.parseUnsignedLong(Long.toUnsignedString(i - k / 2)); l++) {
                        while (temp2 % l == 0) {
                            if (tally_factors.get(l) == null) {
                                tally_factors.put(l, -1);
                            }
                            else {
                                tally_factors.put(l, tally_factors.get(l) - 1);
                            }
                            temp2 = temp2 / l;
                        }
                    }
                    if (tally_factors.get(temp2) == null) {
                        tally_factors.put(temp2, -1);
                    }
                    else {
                        tally_factors.put(temp2, tally_factors.get(temp2) - 1);
                    }
                }
            }
            // result given by multiplying together factor^tally (i.e. key^value) of every Map entry
            long part3 = 1; //bottom of fraction
            for (Long key : tally_factors.keySet()) {
                if (key >= 1) {
                    long part1 = 1; //parts of top of fraction
                    long part2 = 1; // parts of bottom of fraction
                    for (long exp = 1; exp <= Math.abs(tally_factors.get(key)); exp++) {
                        if (tally_factors.get(key) > 0) {
                            part1 = Long.parseUnsignedLong(multiplyLong(part1, key));
                        }
                        else {
                            part2 = Long.parseUnsignedLong(multiplyLong(part2, key));
                        }
                        part1 = Long.divideUnsigned(part1, gcdByEuclidsAlgorithm(part1, part2));
                        part2 = Long.divideUnsigned(part2, gcdByEuclidsAlgorithm(part1, part2));
                    }
                    result = Long.parseUnsignedLong(multiplyLong(result, part1)); //top of fraction
                    part3 = Long.parseUnsignedLong(multiplyLong(part3, part2));
                    result = Long.divideUnsigned(result, gcdByEuclidsAlgorithm(result, part3));
                    part3 = Long.divideUnsigned(part3, gcdByEuclidsAlgorithm(result, part3));
                }
            }
            return Long.toUnsignedString(Long.divideUnsigned(result, part3));
        }
        else {
            return "error: result is greater than 64 bits - maximum result is (2^64)-1";
        }
    }
    /**
     * Takes 2 longs (x and y) and returns the product of multpilying them together one digit at a time, since the
     * answer may be greater than the maximum size for a signed long. The answer is then stored in an array of digits
     * and then returned as String,
     *
     * @param x is the first value
     * @param y is the second value
     * @return String
     */
    public String multiplyLong( long x, long y ) {
        int carry = 0;
        int temp = 0;
        String answer = "";
        List<Integer> digitsx = new ArrayList<Integer>();
        List<Integer> digitsy = new ArrayList<Integer>();
        int m = Long.toUnsignedString(x).length();
        int n = Long.toUnsignedString(y).length();
        int[] result = new int[m + n];
        for (int k = m - 1; k >= 0; k--) {
            digitsx.add(Character.getNumericValue(Long.toUnsignedString(x).charAt(k)));
            result[k] = 0;
        }
        for (int k = n - 1; k >= 0; k--) {
            digitsy.add(Character.getNumericValue(Long.toUnsignedString(y).charAt(k)));
        }
        for (int i = 0; i < n; i++) {
            carry = 0;
            for (int j = 0; j < m; j++) {
                temp = (digitsx.get(j) * digitsy.get(i)) + result[i + j] + carry;
                result[i + j] = temp % 10;
                carry = temp / 10;
            }
            result[i + m] = carry;
        }
        for (int k = n + m - 1; k >= 0; k--) {
            answer += String.valueOf(result[k]);
        }
        return answer;
    }
    /**
     * A support function that takes in a string and returns true,false as to weather it is a digit
     *
     * @param s is the String representation
     * @return boolean if input is a digit
     */
    public boolean isAllDigit( String s ) {
        for (char c : s.toCharArray()) {
            if (!(Character.isDigit(c))) {
                return false;
            }
        }
        return true;
    }
    /**
     * A support function that takes 2 longs and finds the greatest common divisor(gcd) and returns a long
     *
     * @param n1 factor 1
     * @param n2 factor 2
     * @return long the gcd
     */
    public long gcdByEuclidsAlgorithm( long n1, long n2 ) {
        if (n2 == 0) {
            return n1;
        }
        return gcdByEuclidsAlgorithm(n2, Long.remainderUnsigned(n1, n2));
    }
}
