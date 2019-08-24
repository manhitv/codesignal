'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You've launched your brand new web application not long ago, and while in beta it got beta satisfied visitors. Encouraged by such success, you decided to go ahead and push the very first stable version live.
You know that each beta visitor spent at least k minutes on your app, so now you'd like to keep track of new visitors of your web application that spent at least k minutes on it. Given the amount of time the visitors used your application and the value of k, return the total number of users that used your app for at least k minutes including those from beta.
*Example:
For beta = 22, k = 5, and visitors = [4, 6, 6, 5, 2, 2, 5], the output should be countVisitors(beta, k, visitors) = 26.
4 new visitors spent at least 5 minutes on your application, which summed up with 22 satisfied beta users gives 26.
'''
class Counter(object):
    def __init__(self, value):
        self.value = value

    def inc(self):
        self.value += 1

    def get(self):
        return self.value

def countVisitors(beta, k, visitors):
    counter = Counter(beta)
    for visitor in visitors:
        if visitor >= k:
            counter.inc()
    return counter.get()

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Although Python does provide a bunch of useful built-in functions, some of them are simply missing for no apparent reason. One example of such function is a sign function implemented in many other languages. sign(x) returns 1 if x is positive, -1 if x is negative, and 0 if x is equal to zero.
You decided to build your own package of useful functions, and would like to start with the sign function. Given the value of x, return the result of applying the sign function to it.
*Example:
For x = -34, the output should be sign(x) = -1.
-34 is a negative number, thus the output should be -1.
'''
class Functions(object):

    def sign(self):
        if self > 0:
            return 1
        else:
            return -1 if self < 0 else 0

def sign(x):
    return Functions.sign(x)
