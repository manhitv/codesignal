'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions. The message contains several numbers that, when typed into a supercomputer, will launch a missile into the sky blocking out the sun, and making all the people on Earth grumpy and sad.
You figured out that some numbers have a modified single digit in their binary representation. More specifically, in the given number n the kth bit from the right was initially set to 0, but its current value might be different. It's now up to you to write a function that will change the kth bit of n back to 0.
*Example:
For n = 37 and k = 3, the output should be killKthBit(n, k) = 33.
3710 = 1001012 ~> 1000012 = 3310.
For n = 37 and k = 4, the output should be killKthBit(n, k) = 37.
The 4th bit is 0 already (looks like the Mad Coder forgot to encrypt this number), so the answer is still 37.
'''
def killKthBit(n, k):
    return int("".join(list(bin(n)[2:])[:-k] +["0"]+ list(bin(n)[2:])[len(bin(n))-k-1:]),2)

'''
You are given an array of up to four non-negative integers, each less than 256.
Your task is to pack these integers into one number M in the following way:
The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.
Return the obtained integer M.
Note: the phrase "first bits of M" refers to the least significant bits of M - the right-most bits of an integer. For further clarification see the following example.
*Example:
For a = [24, 85, 0], the output should be arrayPacking(a) = 21784.
An array [24, 85, 0] looks like [00011000, 01010101, 00000000] in binary.
After packing these into one number we get 00000000 01010101 00011000 (spaces are placed for convenience), which equals to 21784.
'''
def arrayPacking(a):

    n = ''
    for i in range(len(a) -1, -1, -1):
        m = 8 - len(bin(a[i])[2:])
        n += m*'0' + str(bin(a[i])[2:])
    n = '0b'+ n
    return int(n, 2)

'''
You are given two numbers a and b where 0 ≤ a ≤ b. Imagine you construct an array of all the integers from a to b inclusive. You need to count the number of 1s in the binary representations of all the numbers in the array.
*Example:
For a = 2 and b = 7, the output should be rangeBitCount(a, b) = 11.
Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7]. Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111], which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.
'''
def rangeBitCount(a, b):
    res = []
    while a <= b:
        res.append(bin(a)[2:])
        a += 1
    r = 0
    for e in "".join(res):
        print(int(e))
        r += int(e)
    return r

'''
Reverse the order of the bits in a given integer.
*Example:
For a = 97, the output should be mirrorBits(a) = 67.
97 equals to 1100001 in binary, which is 1000011 after mirroring, and that is 67 in base 10.
For a = 8, the output should be mirrorBits(a) = 1.
'''
def mirrorBits(a):

    s = bin(a)[2:]
    return int(s[::-1], 2)

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Presented with the integer n, find the 0-based position of the second rightmost zero bit in its binary representation (it is guaranteed that such a bit exists), counting from right to left.
Return the value of 2position_of_the_found_bit.
*Example:
For n = 37, the output should be secondRightmostZeroBit(n) = 8.
3710 = 1001012. The second rightmost zero bit is at position 3 (0-based) from the right in the binary representation of n.
Thus, the answer is 23 = 8.
'''
def secondRightmostZeroBit(n):
    return 2**((bin(n)[2:][::-1][:bin(n)[2:][::-1].find('0')]+'_'+bin(n)[2:][::-1][bin(n)[2:][::-1].find('0')+1:]).find('0'))

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You're given an arbitrary 32-bit integer n. Take its binary representation, split bits into it in pairs (bit number 0 and 1, bit number 2 and 3, etc.) and swap bits in each pair. Then return the result as a decimal number.
*Example:
For n = 13, the output should be swapAdjacentBits(n) = 14.
1310 = 11012 ~> {11}{01}2 ~> 11102 = 1410. 
For n = 74, the output should be swapAdjacentBits(n) = 133.
7410 = 010010102 ~> {01}{00}{10}{10}2 ~> 100001012 = 13310.
Note the preceding zero written in front of the initial number: since both numbers are 32-bit integers, they have 32 bits in their binary representation. The preceding zeros in other cases don't matter, so they are omitted. Here, however, it does make a difference.
'''
def swapAdjacentBits(n):
    return int(''.join([ bin(n)[2:][x:x+2][::-1] for x in range(0, len(bin(n)[2:]), 2) ]),2) if len(bin(n)[2:]) % 2 == 0 else int(''.join([   str('0'+ bin(n)[2:])[x:x+2][::-1]  for x in range(0, len(bin(n)[2:])+1, 2) ]),2)

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You're given two integers, n and m. Find position of the rightmost bit in which they differ in their binary representations (it is guaranteed that such a bit exists), counting from right to left.
Return the value of 2position_of_the_found_bit (0-based).
*Example:
For n = 11 and m = 13, the output should be differentRightmostBit(n, m) = 2.
1110 = 10112, 1310 = 11012, the rightmost bit in which they differ is the bit at position 1 (0-based) from the right in the binary representations.
So the answer is 21 = 2.
For n = 7 and m = 23, the output should be differentRightmostBit(n, m) = 16.
710 = 1112, 2310 = 101112, i.e.
00111
10111
So the answer is 24 = 16.
'''
def differentRightmostBit(n, m):
    return 2 **[i for i, e in enumerate(bin(n ^ m)[2:][::-1]) if e == '1'][0]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You're given two integers, n and m. Find position of the rightmost pair of equal bits in their binary representations (it is guaranteed that such a pair exists), counting from right to left.
Return the value of 2position_of_the_found_pair (0-based).
*Example:
For n = 10 and m = 11, the output should be equalPairOfBits(n, m) = 2.
1010 = 10102, 1110 = 10112, the position of the rightmost pair of equal bits is the bit at position 1 (0-based) from the right in the binary representations.
So the answer is 21 = 2.
'''
def equalPairOfBits(n, m):
    return 2 ** [i for i in range(min(len(bin(n)[2:].zfill(30)), len(bin(m)[2:].zfill(30)))) if bin(n)[2:].zfill(30)[::-1][i] == bin(m)[2:].zfill(30)[::-1][i] == '1' or  bin(n)[2:].zfill(30)[::-1][i] == bin(m)[2:].zfill(30)[::-1][i] == '0'][0] if len([i for i in range(min(len(bin(n)[2:].zfill(30)), len(bin(m)[2:].zfill(30)))) if bin(n)[2:].zfill(30)[::-1][i] == bin(m)[2:].zfill(30)[::-1][i] == '1' or  bin(n)[2:].zfill(30)[::-1][i] == bin(m)[2:].zfill(30)[::-1][i] == '0']) > 0 else 2 ** 0
