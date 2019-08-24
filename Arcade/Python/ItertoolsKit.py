'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You've come up with a really cool name for your future startup company, and already have an idea about its logo. This logo will represent a circle, with the prefix of a cyclic string formed by the company name written around it.
The length n of the prefix you need to take depends on the size of the logo. You haven't yet decided on it, so you'd like to try out various options. Given the name of your company, return the prefix of the corresponding cyclic string containing n characters.
*Example:
For name = "nicecoder" and n = 15, the output should be cyclicName(name, n) = "nicecoderniceco".
'''
from itertools import cycle

def cyclicName(name, n):
    gen = cycle(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Not long ago Greg noticed that he started to forget things, and hurried to the doctor. The doc told him that it was perfectly normal for his age, and wrote down a list of pills that Greg can take in order to improve his memory. He especially recommended one medicine as the most effective one.
Unfortunately Greg forgot which medicine is the most effective, and he feels like he really needs to take them. Greg recalls that the name of the most effective medicine goes in the list somewhere after the very first name that has an even length. Your task is to help Greg: given the list of the pills, return a list of three names that go right after the very first medicine name of the even length.
If there are less than three medicines to return, return empty strings instead of them.
*Example:
For pills = ["Notforgetan", "Antimoron", "Rememberin", "Bestmedicen", "Superpillsus"], the output should be memoryPills(pills) = ["Bestmedicen", "Superpillsus", ""].
'''
from itertools import dropwhile

def memoryPills(pills):
    gen = dropwhile(lambda s: len(s) % 2 != 0, pills + [""] * 3)
    next(gen)
    return [next(gen) for _ in range(3)]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
As you may know, the range function in Python allows coders to iterate over elements from start to stop with the given step. Unfortunately it works only for integer values, and additional libraries should be used if a programmer wants to use float values.
CodeSignal doesn't include third-party libraries, so you have to make do with the standard ones. Given float numbers start, stop and step, your task is to return a list of values from start to stop (including start and not including stop), evenly spaced by the step.
Values start, stop and step have at most 5 digits after the decimal point each.
*Example:
For start = -0.9, stop = 0.45, and step = 0.2, the output should be floatRange(start, stop, step) = [-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3].
'''
from itertools import count, takewhile

def floatRange(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
The greatest ever Rock-Paper-Scissors Championship will take place in your town! The best players will battle each other to see who's the best player in the world. Each player will compete against each other player twice, once home and once away.
Given the list of the players, your task is to come up with the list of all the games between them, and return them sorted lexicographically.
*Example:
For players = ["trainee", "warrior", "ninja"], the output should be
rockPaperScissors(players) = [["ninja", "trainee"], ["ninja", "warrior"], 
                              ["trainee", "ninja"], ["trainee", "warrior"], 
                              ["warrior", "ninja"], ["warrior", "trainee"]]
'''
from itertools import permutations

def rockPaperScissors(players):
    return sorted(list(permutations(players, 2)))

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You found your old bike in the attic, and would love to refresh your childhood memories and give it a ride. Unfortunately there is a chain lock on the bike, and the code is a permutation of a set of distinct numbers. Of course, you don't remember it after all these years.
You do remember, however, that the last time you picked up your bike you also couldn't remember the code, so had to run over all possible numbers permutations. Being a programmer, you tried them in the lexicographical order. It took you a couple of days, and in the first day you managed to check k - 1 permutations.
Now that you need to open the lock again, you can start checking the permutations from the kth one. Given the list of numbers, return the kth (1-based) permutation that you should begin with.
*Example:
For numbers = [1, 2, 3, 4, 5] and k = 4, the output should be kthPermutation(numbers, k) = [1, 2, 4, 5, 3].
Here are the first 4 permutations:
[1, 2, 3, 4, 5]
[1, 2, 3, 5, 4]
[1, 2, 4, 3, 5]
[1, 2, 4, 5, 3]
'''
from itertools import permutations

def kthPermutation(numbers, k):
    return list(permutations(numbers))[k-1]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You've been training your whole life, and now your dreams finally came true: you are a member of the best Crazyball team in the world! Unfortunately since your team is one of only two teams that play Crazyball, there are already many players in it, including yourself. For the starting lineup on the upcoming game the coach will pick k players, and you're curious if it's possible for you to make it there.
To calculate the odds of being a starter, you'd like to come up with a list of all possible lineups. Given the list of the players and the number of players k the coach has to pick, return all possible lineups sorted lexicographically. Players in each lineup should also be sorted lexicographically.
*Example:
For players = ["Ninja", "Warrior", "Trainee", "Newbie"] and k = 3,
the output should be
crazyball(players, k) = [["Newbie", "Ninja", "Trainee"], 
                         ["Newbie", "Ninja", "Warrior"], 
                         ["Newbie", "Trainee", "Warrior"], 
                         ["Ninja", "Trainee", "Warrior"]]
'''
from itertools import combinations

def crazyball(players, k):
    return sorted([sorted(i) for i in list(combinations(players, k))])

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You've been trying to crack the password from your friend's laptop (just to prank him, malicious intent!), but with no luck. However, looks like you're finally up to something: you checked the keyboard with the "little detective" game set and determined that the password consists of a limited set of digits.
You've seen your friend typing the password quite a few times, and are now sure that it consists of k digits. You also know that he is very superstitious and believes in the power of number d, so the password is apt to be divisible by it.
Given the digits that comprise the password, its length k and the number d by which it is divisible, return a sorted list of strings that should be tried as passwords.
*Example:
For digits = [1, 5, 2], k = 2, and d = 3, the output should be crackingPassword(digits, k, d) = ["12", "15", "21", "51"].
Here are all the numbers of length 2: 11, 15, 12, 51, 55, 52, 21, 25 and 22. Only four of them are divisible by 3, and they comprise the answer.
'''
from itertools import product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(["".join(i) for i in list(product(createNumber(digits), repeat=k)) if int("".join(i))%d==0])
