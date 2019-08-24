'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
A grand Team Chess Tournament will be held at your University. Two teams, smarties and cleveries, will clash to determine whose chess skills are better. The teams have the same number of members, and the ith member of smarties will play against the ith member of cleveries in the ith game for each valid i
Given the names of the players of both smarties and cleveries, return the games in the order they will be played.
*Example:
For smarties = ["Jane", "Bob", "Peter"] and cleveries = ["Oscar", "Lidia", "Ann"], the output should be
chessTeams(smarties, cleveries) = [["Jane",  "Oscar"],
                                   ["Bob",   "Lidia"],
                                   ["Peter", "Ann"]]
'''
def chessTeams(smarties, cleveries):
    return list(zip(smarties, cleveries))

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Your teacher asked you to implement a function that calculates the Answer to the Ultimate Question of Life, the Universe, and Everything and returns it as an array of integers. After several hours of hardcore coding you managed to write such a function, and it produced a quite reasonable result. However, when you decided to compare your answer with results of your classmates, you discovered that the elements of your result are roughly 10 times greater than the ones your peers got.
You don't have time to investigate the problem, so you need to implement a function that will fix the given array for you. Given result, return an array of the same length, where the ith element is equal to the ith element of result with the last digit dropped.
*Example:
For result = [42, 239, 365, 50], the output should be fixResult(result) = [4, 23, 36, 5].
'''
def fixResult(result):
    def fix(x):
        return x // 10

    return list(map(fix, result))

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
John has just entered a college, and should now pick several courses to take. He knows nothing, except that number x is a bad luck for him, which is why he won't even consider courses whose title consist of x letters.
Given a list of courses, remove the courses with titles consisting of x letters and return the result.
*Example:
For x = 7 and courses = ["Art", "Finance", "Business", "Speech", "History", "Writing", "Statistics"],
the output should be collegeCourses(x, courses) = ["Art", "Business", "Speech", "Statistics"].
'''
def collegeCourses(x, courses):
    def shouldConsider(course):
        return len(course) != x

    return list(filter(shouldConsider, courses))

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You noticed that one of your employees has a weird performance rate: although his performance is usually good and stable, from time to time it drops drastically. You suspect it has something to do with the famous Code of Clones series: new episodes started to come out recently, and everyone watches and rewatches them every so often.
To confirm your theory, you'd like to create a histogram showing the number of assignments he completed each day in the given period. Given this assignments, return a list representing a horizontal histogram, where each bar is formed by the given character ch.
*Example:
For ch = '*' and assignments = [12, 12, 14, 3, 12, 15, 14], the output should be
createHistogram(ch, assignments) = ["************",
                                    "************",
                                    "**************",
                                    "***",
                                    "************",
                                    "***************",
                                    "**************"]
'''
def createHistogram(ch, assignments):
    return [ch * i for i in assignments]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You need to sum up a bunch of fractions that have different denominators. In order to do this, you need to find the least common denominator of all the fractions. As a professional programmer, you know that the least common denominator is in fact their LCM.
For the given list of denominators, find the least common denominator by finding their LCM.
*Example:
For denominators = [2, 3, 4, 5, 6], the output should be leastCommonDenominator(denominators) = 60.
'''
from fractions import gcd

def leastCommonDenominator(denominators):
    return functools.reduce(lambda x,y: x * y/ gcd(x,y), denominators)
