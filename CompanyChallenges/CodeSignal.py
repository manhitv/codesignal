'''
Each CodeSignal Company Bot is trained by engineers from that specific company. The way it works is that a representative group of engineers from each company is identified as trainers before the bot goes live, and they CodeFight against the bot during a training phase. The current training algorithm is definitely more complex, but let's assume it works this way:
For each trainer we collect two pieces of information per task [answerTime, correctness], where correctness is 1 if the answer was correct, -1 if the answer was wrong, and 0 if no answer was given. In this case, the bot's correct answer time for a given task would be the average of the answer times from the trainers who answered correctly. Given all of the training information for a specific task, calculate the bot's answer time.
*Example:
For
trainingData = [[3, 1],
                [6, 1],
                [4, 1],
                [5, 1]]
the output should be companyBotStrategy(trainingData) = 4.5.
All four trainers have solved the task correctly, so the answer is (3 + 6 + 4 + 5) / 4 = 4.5.
For
trainingData = [[4, 1],
                [4, -1],
                [0, 0],
                [6, 1]]
the output should be companyBotStrategy(trainingData) = 5.0.
Only the 1st and the 4th trainers (1-based) submitted correct solutions, so the answer is (4 + 6) / 2 = 5.0.
For
trainingData = [[4, -1],
                [0, 0],
                [5, -1]]
the output should be companyBotStrategy(trainingData) = 0.0.
No correct answers were given for the task.
'''
def companyBotStrategy(trainingData):

    a = []
    for i in range(len(trainingData)):
        if trainingData[i][1] == 1:
            a.append(trainingData[i][0])
    if len(a) == 0:
        return 0
    else: 
        return sum(a)/len(a)
            
'''
CodeSignal supports different challenge types. One of them asks you to find a bug on a single line of the given code, usually referred to as a DEBUGGING challenge. Behind the scenes, we correctly implement each challenge ourselves and then use special comments with specific prefixes to introduce the buggy lines. Here is an image to help you visualize what that looks like:
As you can see, each of the special comments looks like this:
<spaces>//DB <id>//<buggy line>
where <spaces> is a string consisting of zero or more spaces (for indentation), DB indicates that this comment is for a DEBUGGING challenge (let's assume this is the only type we support), id is a positive integer that helps us enumerate these and <buggy line> is some code that's almost identical to the line to be replaced but with an inserted bug (that is guaranteed not to contain any '/' symbols).
When importing these to our database, each of the special comments is used to create a debugging challenge. The importing script looks for the last non-special-comment line above the special comment and replaces it with "<spaces><buggy line>" while removing all the other special comments from the code. Examples below can help clarify this process further.
Your task is to produce DEBUGGING challenges given source code that includes the special comments and the id of the desired DEBUGGING challenge.
*Example:
For
source = ["ans = 0",
          "for i in range(n):",
          "    for j in range(n):",
          "    //DB 3//for j in range(1, n):",
          "    //DB 2//for j in range(n + 1):",
          "        ans += 1",
          "return ans"]
and challengeId = 3, the output should be
taskMaker(source, challengeId) = ["ans = 0",
                                  "for i in range(n):",
                                  "    for j in range(1, n):",
                                  "        ans += 1",
                                  "return ans"]
For
source = ["ans = 0;",
          "for (var i = 0; i < n; i++) {",
          "    for (var j = 0; j < n; j++) {",
          "    //DB 3//for (var j = 1; j < n; j++) {",
          "    //DB 2//for (var j = 0; j < n + 1; j++) {",
          "        ans++;",
          "    }",
          "}",
          "return ans;"]
and challengeId = 2, the output should be
taskMaker(source, challengeId) = ["ans = 0;",
                                  "for (var i = 0; i < n; i++) {",
                                  "    for (var j = 0; j < n + 1; j++) {",
                                  "        ans++;",
                                  "    }",
                                  "}",
                                  "return ans;"]
'''
def taskMaker(source, challengeId):
    
    chalString = '//DB ' + str(challengeId) + '//'

    out = []
    for ln in source:
        if ln.strip()[0:2]=='//':
            if ln.strip()[0:len(chalString)]==chalString:
                out.pop()
                out.append(ln.replace(chalString,''))
        else:
            out.append(ln)

    return(out)

'''
In CodeSignal marathons, each task score is calculated independently. For a specific task, you get some amount of points if you solve it correctly, or you get a 0. Here is how the exact number of points is calculated:
If you solve a task on your first attempt within the first minute, you get maxScore points.
Each additional minute you spend on the task adds a penalty of (maxScore / 2) * (1 / marathonLength) to your final score.
Each unsuccessful attempt adds a penalty of 10 to your final score.
After all the penalties are deducted, if the score is less than maxScore / 2, you still get maxScore / 2 points.
Implement an algorithm that calculates this score given some initial parameters.
*Example:
For
marathonLength = 100,
maxScore = 400,
submissions = 4, and
successfulSubmissionTime = 30, the output should be
marathonTaskScore(marathonLength, maxScore, submissions, successfulSubmissionTime) = 310.
Three unsuccessful attempts cost 10 * 3 = 30 points. 30 minutes adds 30 * (400 / 2) * (1 / 100) = 60 more points to the total penalty. So the final score is 400 - 30 - 60 = 310.
For
marathonLength = 100,
maxScore = 400,
submissions = 95, and
successfulSubmissionTime = 30, the output should be
marathonTaskScore(marathonLength, maxScore, submissions, successfulSubmissionTime) = 200.
400 - 10 * 94 - 30 * (400 / 2) * (1 / 100) = -600. But the score for this task cannot be less than 400 / 2 = 200, so the final score is 200 points.
For marathonLength = 100, maxScore = 400, submissions = 95, and successfulSubmissionTime = -1, the output should be
marathonTaskScore(marathonLength, maxScore, submissions, successfulSubmissionTime) = 0.
The task wasn't solved, so it doesn't give any points.
'''
def marathonTaskScore(marathonLength, maxScore, submissions, successfulSubmissionTime):

    if successfulSubmissionTime < 0:
        return 0
    if successfulSubmissionTime <= 1:
        if submissions == 1:
            return maxScore
        else: 
            return max(maxScore/2, maxScore - 10*(submissions-1))
    else:
        return max(maxScore/2, maxScore - successfulSubmissionTime*maxScore/2/marathonLength - 10*(submissions-1))
