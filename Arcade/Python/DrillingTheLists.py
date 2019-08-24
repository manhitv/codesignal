'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Billy and Mandy are twins, and as such they do everything together. Unfortunately during the finals they were forced to write their exams separately, which explains why they got such low scores. However, they are not too sad about it: since they are twins, it's only natural for them to work together, so they are going to sum up their scores for each exam and show them to their mom.
Given two lists of equal size representing the scores Billy and Mandy got for each exam (b and m, respectively), return a single list containing their combined score.
*Example:
For b = [22, 13, 45, 32] and m = [28, 41, 13, 32], the output should be twinsScore(b, m) = [50, 54, 58, 64].
'''
def twinsScore(b, m):
    return [b[i] + m[i] for i in range(len(b))]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Harry dropped out of school to pursue his dreams and work in Pipes Corporations. He is now in charge of a lot of pipes, and his task is to check the gauges twice a day. By analyzing the morning and evening pressures of each pipe, Harry should write a report about the minimum and the maximum pressure during the day.
Given the pressures Harry wrote down for each pipe, return two lists: the first one containing the minimum, and the second one containing the maximum pressure of each pipe during the day.
*Example:
For morning = [3, 5, 2, 6] and evening = [1, 6, 6, 6], the output should be pressureGauges(morning, evening) = [[1, 5, 2, 6], [3, 6, 6, 6]].
'''
def pressureGauges(morning, evening):
    return [[min(u, v) for u, v in zip(morning, evening)], [max(u, v) for u, v in zip(morning, evening)]]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
For the opening ceremony of the upcoming sports event an even number of athletes were picked. They formed a correct lineup, i.e. such a lineup in which no two boys or two girls stand together. The first person in the lineup was a girl. As a part of the performance, adjacent pairs of athletes (i.e. the first one together with the second one, the third one together with the fourth one, etc.) had to swap positions with each other.
Given a list of athletes, return the list of athletes after the changes, i.e. after each adjacent pair of athletes is swapped.
*Example:
For athletes = [1, 2, 3, 4, 5, 6], the output should be correctLineup(athletes) = [2, 1, 4, 3, 6, 5].
'''
def correctLineup(athletes):
    return [j for i in zip(athletes[1::2], athletes[0::2]) for j in i]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You're organizing a group dating activity for cats, i.e. a meeting where an equal number of male and female cats get together. For each cat you calculate their nature value, an integer that describes the cat's spirit. When a male and a female cat with the same nature value see each other, they become connected and happily walk out together.
You've just started another group dating, and placed the cats in front of one another so that the ith male is sitting across the ith female. What cats will remain at their places, assuming that the pairs of cats sitting in front of each other and having the same nature values will walk out?
*Example:
For male = [5, 28, 14, 99, 17] and female = [5, 14, 28, 99, 16],
the output should be groupDating(male, female) = [[28, 14, 17], [14, 28, 16]].
Pairs of cats at positions 0 and 3 (0-based) have the same nature values, so they will leave the meeting.
'''
def groupDating(male, female):
    return [[male[i] for i in range(len(male)) if male[i] != female[i]], 
            [female[i] for i in range(len(male)) if female[i] != male[i]]]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Not long ago a young Christmas elf asked you to implement a function that creates Christmas trees made of asterisks ('*') similar to the one below:
    *    
    *    
   ***   
  *****  
 ******* 
*********
   ***   
Unfortunately because of the extreme coldness the tree that you sent over was corrupted: although its lines are given in the correct order, but are not aligned properly. Now your task is to fix the given tree by centering the asterisks in each line.
*Example:
For
tree = [
  "      *  ", 
  "    *    ", 
  "***      ", 
  "    *****", 
  "  *******", 
  "*********", 
  " ***     "
]
the output should be
fixTree(tree) = [
  "    *    ", 
  "    *    ", 
  "   ***   ", 
  "  *****  ", 
  " ******* ", 
  "*********", 
  "   ***   "
]
'''
def fixTree(tree):
    return [(len(i)-i.count('*'))//2*' ' + i.count('*')*'*' + (len(i)-i.count('*'))//2*' '
            for i in tree]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
There is a great technique that allows finding sums of consecutive elements in the given array extremely fast. It is based on the usage of prefix sums. Given array a, your task is to calculate all its prefix sums.
*Example:
For a = [1, 2, 3], the output should be prefSum(a) = [1, 3, 6].
Here's how the prefix sums can be calculated: [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6].
'''
def prefSum(a):
    return [ [a,a.append(x+a.pop())][0][-1] for x in [a,a.append(0),a][0][:-1] ]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Little Billy is not too good with numbers and having trouble even multiplying and adding them. He needs some practice, and you are the one helpful fellow who can give him a list of numbers to practice on. Given a list of numbers, Billy should calculate the following value:
(((...(a[0] + a[1]) * a[2] + a[3]) * a[4] + ...)
Unfortunately you yourself are not too good with math, but you know how to code. Implement a function that, given a list of numbers, will return the result of the operation Billy has to perform.
*Example:
For numbers = [1, 2, 3, 4, 5, 6], the output should be mathPractice(numbers) = 71.
Here's how the answer is obtained: ((1 + 2) * 3 + 4) * 5 + 6 = 71.
'''
def mathPractice(numbers):
    return functools.reduce(lambda acc,x: (acc+x[1] if x[0]%2 else acc*x[1]), enumerate(numbers), 1)
