'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
To make debug output more understandable, you often separate sets of logs by a single line of the same character. Since you use this method very often, you'd like to write a function that would handle printing the separator.
Implement a function that, given a character ch and the number of times it should be repeated n, returns a string of n characters ch.
*Example:
For ch = '*' and n = 20, the output should be repeatChar(ch, n) = "********************".
'''
repeatChar = lambda c,n: c*n

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
A new scoring system was introduced in your university: from now on, each test will consist of the predefined list of questions, and for the ith (1-based) question a student either gets i points, or loses p points as a penalty.
Your task is to calculate the number of points a student got for some test. Implement a function that would calculate the number of points received for the test based on the given list of answers.
*Example:
For answers = [true, true, false, true]and p = 2, the output should be getPoints(answers, p) = 5.
Here's why: 1 + 2 - 2 + 4 = 5.
'''
def getPoints(answers, p):
    questionPoints = lambda i, ans: i+1 if ans else -1*p

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You are given a list of students who want to apply to the internship at CodeSignal. For the ith student you know their full name students[i], which can consist of up to 5 words (where a word is a set of consecutive letters). It is guaranteed that the surname is always the last name of student's full name.
Your task is to sort the students lexicographically by their surnames. If two students happen to have the same surname, their order in the result should be the same as in the original list.
*Example:
For
students = ["John Smith", "Jacky Mon Simonoff", 
            "Lucy Smith", "Angela Zimonova"]
the output should be
sortStudents(students) = ["Jacky Mon Simonoff", "John Smith", 
                          "Lucy Smith", "Angela Zimonova"]
'''
def sortStudents(students):
    students.sort(key=lambda x : x.split(' ')[-1])
    return students

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You've been preparing all night for the upcoming test and entered the class certain that you will ace it. Now that you received the test questions, you died inside a little: looks like you prepared for the test on a completely different topic.
You're not even sure if you should bother to answer the questions. You still have some hope though: it is known that there's a glitch in the test preparing system, so that if the sum of digits of question ids is divisible by k, the answer to each question has a 90% probability to be an A.
Given the list of question ids, determine if the sum of their digits is divisible by k to see if it's worth trying to pass the test.
*Example:
For ids = [529665, 909767, 644200] and k = 3, the output should be isTestSolvable(ids, k) = true.
The sum of digits is (5 + 2 + 9 + 6 + 6 + 5) + (9 + 0 + 9 + 7 + 6 + 7) + (6 + 4 + 4 + 2 + 0 + 0) = 87
which is divisible by 3. Today is your lucky day after all!
'''
def isTestSolvable(ids, k):
    digitSum = lambda questionId: sum(int(x) for x in str(questionId)) 

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
