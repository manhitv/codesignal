'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You are working on a revolutionary video game. In this game the player will be able to collect several types of bonuses on each level, and his total score for the level is equal to the sum of the first n bonuses he collected. However, if he collects less than n bonuses, his score will be equal to 0.
Given the bonuses the player got, your task is to return his final score for the level.
*Example:
For bonuses = [4, 2, 4, 5] and n = 3, the output should be calcBonuses(bonuses, n) = 10.
4 + 2 + 4 = 10.
For bonuses = [4, 2, 4, 5] and n = 5, the output should be calcBonuses(bonuses, n) = 0.
The player has collected only 4 bonuses, so his final score is 0.
'''
def calcBonuses(bonuses, n):
    it = iter(bonuses)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You are working on a revolutionary video game. This game will consist of several levels, and on each level the player will be able to collect bonuses. For each passed level the player will thus get some score, determined by the number of collected bonuses.
Player's final score is decided by the number of completed levels and scores obtained on each of them. The final score is calculated as the sum of squares of n maximum scores obtained. If the number of completed levels is less than n, the score is calculated as the sum of squared scores for each level, and final result is divided by 5 as a penalty (the result is rounded down to the nearest integer).
Given the list of scores the player got for completed levels and the number n that determines the number of levels you have to pass to avoid being penalized, return the player's final game score.
*Example:
For scores = [4, 2, 4, 5] and n = 3, the output should be calcFinalScore(scores, n) = 57.
52 + 42 + 42 = 57.
For scores = [4, 2, 4, 5] and n = 5, the output should be calcFinalScore(scores, n) = 12.
(42 + 22 + 42 + 52) / 5 = 61 / 5 ≈ 12.
'''
def calcFinalScore(scores, n):
    gen = (i**2 for i in sorted(scores)[::-1])

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Fibonacci sequence is known to every programmer, and you're not an exception. It is believed that not all properties of Fibonacci numbers are yet studied, and in order to help your descendants, you'd like to implement a generator that will generate Fibonacci numbers infinitely. Who knows, maybe in the distant future your generator will help to make a breakthrough in this field!
To test your generator, you'd like to check the first few values. Given the number n, return the first n numbers of Fibonacci sequence.
*Example:
For n = 3, the output should be fibonacciGenerator(n) = [0, 1, 1].
The first three Fibonacci numbers are 0, 1 and 1.
'''
def fibonacciGenerator(n):
    def fib():
        last = (0, 1)
        while True:
            yield last[0]
            last = last[0] + last[1], last[0]

    gen = fib()
    return [next(gen) for _ in range(n)]
