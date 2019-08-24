'''
Given an integer n, find the minimal k such that
k = m! (where m! = 1 * 2 * ... * m) for some integer m;
k >= n.
In other words, find the smallest factorial which is not less than n.
*Example:
For n = 17, the output should be leastFactorial(n) = 24.
17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).
'''
def leastFactorial(n):

    fac = 1
    if n == 1:
        return 1
    for i in range(1, n):
        fac *= i
        if fac >= n:
            return fac

'''
Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.
*Example:
For n = 6, l = 2, and r = 4, the output should be countSumOfTwoRepresentations2(n, l, r) = 2.
There are just two ways to write 6 as A + B, where 2 ≤ A ≤ B ≤ 4: 6 = 2 + 4 and 6 = 3 + 3.
'''
def countSumOfTwoRepresentations2(n, l, r):
    temp = 0
    if l <= n//2 <= r:
        if n%2 == 0:
            return min([(n//2-l)+1,(r-n//2)+1])
        else:
            return min([(n//2-l),(r-n//2)])
    else:
        return 0

'''
You are standing at a magical well. It has two positive integers written on it: a and b. Each time you cast a magic marble into the well, it gives you a * b dollars and then both a and b increase by 1. You have n magic marbles. How much money will you make?
*Example:
For a = 1, b = 2, and n = 2, the output should be magicalWell(a, b, n) = 8.
You will cast your first marble and get $2, after which the numbers will become 2 and 3. When you cast your second marble, the well will give you $6. Overall, you'll make $8. So, the output is 8.
'''
def magicalWell(a, b, n):
    if n==0:
        return 0
    s = 0
    for i in range(n):
           s += (a+i)*(b+i)
    return s

'''
To prepare his students for an upcoming game, the sports coach decides to try some new training drills. To begin with, he lines them up and starts with the following warm-up exercise: when the coach says 'L', he instructs the students to turn to the left. Alternatively, when he says 'R', they should turn to the right. Finally, when the coach says 'A', the students should turn around.
Unfortunately some students (not all of them, but at least one) can't tell left from right, meaning they always turn right when they hear 'L' and left when they hear 'R'. The coach wants to know how many times the students end up facing the same direction.
Given the list of commands the coach has given, count the number of such commands after which the students will be facing the same direction.
*Example:
For commands = "LLARL", the output should be lineUp(commands) = 3.
Let's say that there are 4 students, and the second one can't tell left from right. In this case, only after the second, third and fifth commands will the students face the same direction.
'''
def lineUp(a):
    size = len(a)
    deg = 0
    temp = 0
    for i in range(0,size):
        if a[i] == 'L':
            deg += -90
        elif a[i] == 'R':
            deg += 90
        elif a[i] == 'A':
            deg += 180
        if deg%180==0:
            temp += 1
            deg = 0
    return temp

'''
A little boy is studying arithmetics. He has just learned how to add two integers, written one below another, column by column. But he always forgets about the important part - carrying.
Given two integers, your task is to find the result which the little boy will get.
Note: The boy had learned from this site, so feel free to check it out too if you are not familiar with column addition.
*Example:
For param1 = 456 and param2 = 1734, the output should be additionWithoutCarrying(param1, param2) = 1180.
   456
  1734
+ ____
  1180
The boy performs the following operations from right to left:
6 + 4 = 10 but he forgets about carrying the 1 and just writes down the 0 in the last column
5 + 3 = 8
4 + 7 = 11 but he forgets about the leading 1 and just writes down 1 under 4 and 7.
There is no digit in the first number corresponding to the leading digit of the second one, so the boy imagines that 0 is written before 456. Thus, he gets 0 + 1 = 1.
'''
def additionWithoutCarrying(param1, param2):
    p1, p2, p = str(param1), str(param2), ''
    if len(p2) > len(p1):
        p1 = (len(p2) - len(p1))*'0' + p1
    else:
        p2 = (len(p1) - len(p2))*'0' + p2
    for i, j in zip(p1, p2):
        p += str((int(i) + int(j))%10)
    return int(p)

'''
You have k apple boxes full of apples. Each square box of size m contains m × m apples. You just noticed two interesting properties about the boxes:
The smallest box is size 1, the next one is size 2,..., all the way up to size k.
Boxes that have an odd size contain only yellow apples. Boxes that have an even size contain only red apples.
Your task is to calculate the difference between the number of red apples and the number of yellow apples.
*Example:
For k = 5, the output should be appleBoxes(k) = -15.
There are 1 + 3 * 3 + 5 * 5 = 35 yellow apples and 2 * 2 + 4 * 4 = 20 red apples, making the answer 20 - 35 = -15.
'''
def appleBoxes(k):
    s = [i for i in range(1, k+1)]
    a = sum([s[i]**2 - s[i-1]**2 for i in range(1, k, 2)])
    return -k**2 + a if k%2 else a
        
'''
Define an integer's roundness as the number of trailing zeroes in it.
Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.
*Example:
For n = 902200100, the output should be increaseNumberRoundness(n) = true.
One of the possible ways to increase roundness of n is to swap digit 1 with digit 0 preceding it: roundness of 902201000 is 3, and roundness of n is 2.
For instance, one may swap the leftmost 0 with 1.
For n = 11000, the output should be increaseNumberRoundness(n) = false.
Roundness of n is 3, and there is no way to increase it.
'''
def increaseNumberRoundness(n):

    return '0' in str(n).rstrip('0')
            
'''          
We want to turn the given integer into a number that has only one non-zero digit using a tail rounding approach. This means that at each step we take the last non 0 digit of the number and round it to 0 or to 10. If it's less than 5 we round it to 0 if it's larger than or equal to 5 we round it to 10 (rounding to 10 means increasing the next significant digit by 1). The process stops immediately once there is only one non-zero digit left.
*Example:
For n = 15, the output should be rounders(n) = 20;
For n = 1234, the output should be rounders(n) = 1000.
1234 -> 1230 -> 1200 -> 1000.
For n = 1445, the output should be rounders(n) = 2000.
1445 -> 1450 -> 1500 -> 2000.
'''
def rounders(n):
    x = 1
    while n > 10:
        n = (n + 5) // 10
        x *= 10
    return x * n

'''
When a candle finishes burning it leaves a leftover. makeNew leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.
You have candlesNumber candles in your possession. What's the total number of candles you can burn, assuming that you create new candles as soon as you have enough leftovers?
*Example:
For candlesNumber = 5 and makeNew = 2, the output should be candles(candlesNumber, makeNew) = 9.
Here is what you can do to burn 9 candles:
burn 5 candles, obtain 5 leftovers;
create 2 more candles, using 4 leftovers (1 leftover remains);
burn 2 candles, end up with 3 leftovers;
create another candle using 2 leftovers (1 leftover remains);
burn the created candle, which gives another leftover (2 leftovers in total);
create a candle from the remaining leftovers;
burn the last candle.
Thus, you can burn 5 + 2 + 1 + 1 = 9 candles, which is the answer.
'''
def candles(candlesNumber, makeNew):

    return candlesNumber + (candlesNumber - 1) // (makeNew - 1)

'''
Imagine a white rectangular grid of n rows and m columns divided into two parts by a diagonal line running from the upper left to the lower right corner. Now let's paint the grid in two colors according to the following rules:
A cell is painted black if it has at least one point in common with the diagonal;
Otherwise, a cell is painted white.
Count the number of cells painted black.
*Example:
For n = 3 and m = 4, the output should be countBlackCells(n, m) = 6.
There are 6 cells that have at least one common point with the diagonal and therefore are painted black.
For n = 3 and m = 3, the output should be countBlackCells(n, m) = 7.
7 cells have at least one common point with the diagonal and are painted black.
'''
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def countBlackCells(n, m):
    return n + m + gcd(n,m) - 2
