'''
You've just started constructing a military academy. It will take t seconds to erect the building, but given that you're in a hurry you decide this is too long to wait.
Fortunately, your Alliance offers you help to speed up construction - this is called a boost. Each member of the Alliance can decrease the time needed to finish the building either by 10% of the initial construction time or by 1 minute (whichever is greater). However, you can't get more than 10 boosts for a given construction project. Assuming that your Alliance members act optimally, find the shortest possible time it will take to build the academy.
Note:
If 10% of the total construction time doesn't equal an integer number of seconds, then the time bonus you get is rounded down (for each of the Alliance members independently).
If time decreased using boosts becomes negative you should return 0.
*Example:
For t = 1000 and allianceSize = 10, the output should be allianceHelp(t, allianceSize) = 0.
If each member of the Alliance boosts the building by 10% (i.e. by 100 seconds), your new academy will be finished instantly.
For t = 999 and allianceSize = 11, the output should be allianceHelp(t, allianceSize) = 9.
Any 10 of your 11 allies can speed the construction up by 10% (which equals 99 seconds since 99.9 is rounded down).
For t = 100 and allianceSize = 1, the output should be allianceHelp(t, allianceSize) = 40.
Your only Alliance member will boost the construction by 1 minute (i.e. 60 seconds).
'''
def allianceHelp(t, allianceSize):

    time = int(t//10) if int(t//10) > 60 else 60
    size = allianceSize if allianceSize < 10 else 10
    result = t - time*size
    return result if result > 0 else 0

'''           
As part of a successful war campaign you just took control of a major city. This is where you will make your new Forward Operating Base, and where your troops will house their new barracks. However, when your troops are in the city they consume k units of food (for some integer k) as upkeep at the beginning of every hour (i.e. at HH:00:00 where HH stands for an hour). This upkeep happens even when you're offline and not actively playing.
Given the timestamps of logout and login performed consecutively and the amount of food you had at those moments, find how much food your troops consume each hour.
For simplicity's sake, assume that you are neither logged in nor logged out at the beginning of each hour.
*Example:
For logOut = [1451604600, 100] and logIn = [1451660401, 36], the output should be resourceCatchUp(logOut, logIn) = 4.
1451604600 corresponds to 31 December, 2015, 23:30:00;
1451660401 corresponds to 1 January, 2016, 15:00:01;
thus, food consumption took place exactly 16 times while you were logged out;
your amount of food was reduced by 64 units. This means that each hour your troops consumed 4 units of food.
'''
def resourceCatchUp(logOut, logIn):

    from datetime import datetime
    log = datetime.fromtimestamp(logIn[0]) - datetime.fromtimestamp(logOut[0])
    
    hours = 24*log.days + math.ceil(log.seconds/float(3600))
    return (logOut[1] - logIn[1])/hours

'''
Sometimes a player is offered so many quests during a game that it's difficult to complete them all. Time is short, and naturally each player wants to complete as many quests as possible while maximizing the points they earn. Here is the scenario:
PlayerOne has a long list of quests, but only timeForQuests hours to complete them. The ith quest should be completed in hi hours, and the reward for it is pointsi. Each quest can be completed only once. Calculate the maximum number of points that PlayerOne can earn.
*Example:
For h = [1, 4, 2], points = [2, 3, 2], and timeForQuests = 4, the output should be questEfficiencyItem(h, points, timeForQuests) = 4.
PlayerOne has 4 hours to complete the quests, so it is possible to earn:
2 points for the first quest;
3 points for the second quest;
2 points for the third quest;
2 + 2 = 4 points for the first and the third quests.
So, the maximum number of points PlayerOne can earn is 4.
For h = [1, 4, 2], points = [2, 5, 2], and timeForQuests = 4, the output should be questEfficiencyItem(h, points, timeForQuests) = 5.
Completing the second quest gives 5 points, which is greater than solving the first and the third quests (2 + 2 = 4 points).
'''
def questEfficiencyItem(h, points, timeForQuests):
    memo = [[0 for _ in range(timeForQuests+1)] for _ in range(len(h)+1)]
    for i in range(1, len(h)+1):
        for j in range(timeForQuests+1):
            if h[i-1] > j:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = max(memo[i-1][j], memo[i-1][j-h[i-1]] + points[i-1])
    return memo[-1][-1]https://app.codesignal.com/company-challenges/mz

'''
Picture a map of a battlefield divided into two halves. Points which lie to the left of the line x = 0 are on the forest free side, while points which lie on or to the right of the line are in the forest.
Your army needs to get from point a to point b. The problem is that while point a is located on the forest free side where your army's speed equals v1 miles per hour, point b is located in the forest, where your speed reduces to v2 miles per hour.
Calculate the shortest possible travel time for your army to reach point b.
*Example:
For a = [-1.5, 0.5], b = [1.5, 1.5], v1 = 4.4, and v2 = 1.1, the output should be armyMarch(a, b, v1, v2) = 1.761942.
'''
def armyMarch(a, b, v1, v2):

    from math import sqrt
    min_t = sqrt(a[0]**2 + a[1]**2)/v1 + sqrt(b[0]**2 + b[1]**2)/v2 
    if a[1] == b[1]:
        return sqrt(a[0]**2)/v1 + sqrt(b[0]**2)/v2
    max_y, min_y = max(a[1], b[1]), min(a[1], b[1])
    for i in range(int(10000*min_y), int(10000*max_y)+1):
        t = sqrt((a[0]**2 + (float(i/10000)-a[1])**2))/v1 + sqrt((b[0]**2 + (float(i/10000)-b[1])**2))/v2
        if t < min_t:
            min_t = t
    return min_t
