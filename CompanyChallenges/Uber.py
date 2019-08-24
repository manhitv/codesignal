'''
Uber is building a Fare Estimator that can tell you how much your ride will cost before you request it. It works by passing approximated ride distance and ride time through this formula:
(Cost per minute) * (ride time) + (Cost per mile) * (ride distance)
where Cost per minute and Cost per mile depend on the car type.
You are one of the engineers building the Fare Estimator, so knowing cost per minute and cost per mile for each car type, as well as ride distance and ride time, return the fare estimates for all car types.
*Example:
For
ride_time = 30,
ride_distance = 7,
cost_per_minute = [0.2, 0.35, 0.4, 0.45], and
cost_per_mile = [1.1, 1.8, 2.3, 3.5], the output should be
fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile) = [13.7, 23.1, 28.1, 38].
Since:
30 * 0.2 + 7 * 1.1 = 6 + 7.7 = 13.7
30 * 0.35 + 7 * 1.8 = 10.5 + 12.6 = 23.1
30 * 0.4 + 7 * 2.3 = 12 + 16.1 = 28.1
30 * 0.45 + 7 * 3.5 = 13.5 + 24.5 = 38
'''
def fareEstimator(ride_time, ride_distance, cost_per_minute, cost_per_mile):
    s =[]
    for i in range(len(cost_per_minute)):
        s.append(ride_time*cost_per_minute[i] + ride_distance*cost_per_mile[i])
    return s

'''
Consider a city where the streets are perfectly laid out to form an infinite square grid. In this city finding the shortest path between two given points (an origin and a destination) is much easier than in other more complex cities. As a new Uber developer, you are tasked to create an algorithm that does this calculation.
Given user's departure and destination coordinates, each of them located on some street, find the length of the shortest route between them assuming that cars can only move along the streets. Each street can be represented as a straight line defined by the x = n or y = n formula, where n is an integer.
*Example:
For departure = [0.4, 1] and destination = [0.9, 3], the output should be
perfectCity(departure, destination) = 2.7.
0.6 + 2 + 0.1 = 2.7, which is the answer.
'''
def perfectCity(s,f):
    if int(s[1])==s[1]:
        x = math.ceil(min(s[0],f[0]))
        y = math.floor(max(s[0],f[0]))
        return abs(s[1]-f[1])+min(abs(x-s[0])+abs(x-f[0]),abs(y-s[0])+abs(y-f[0]))
    else:
        x = math.ceil(min(s[1],f[1]))
        y = math.floor(max(s[1],f[1]))
        return abs(s[0]-f[0])+min(abs(x-s[1])+abs(x-f[1]),abs(y-s[1])+abs(y-f[1]))

'''
Being a new Uber user, you have $20 off your first ride. You want to make the most out of it and drive in the fanciest car you can afford, without spending any out-of-pocket money. There are 5 options, from the least to the most expensive: "UberX", "UberXL", "UberPlus", "UberBlack" and "UberSUV".
You know the length l of your ride in miles and how much one mile costs for each car. Find the best car you can afford.
*Example:
For l = 30 and fares = [0.3, 0.5, 0.7, 1, 1.3], the output should be fancyRide(l, fares) = "UberXL".
The cost for the ride in this car would be $15, which you can afford, but "UberPlus" would cost $21, which is too much for you.
'''
def fancyRide(l, fares):
    max_fare = 20
    cars = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
    arr = [l * e for e in fares]
    class_ = 0
    for i, e in enumerate(arr):
        if e <= max_fare:
            class_ = i
    return cars[class_]
