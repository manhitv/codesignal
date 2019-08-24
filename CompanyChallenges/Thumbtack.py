'''
In Thumbtack, users are able to rate Pros based on their experience working with them. Each rating is an integer ranging from 1 to 5, and all ratings are averaged to produce a single number rating for any given Pro. Those Pros who have a rating lower than a specified threshold are manually reviewed by Thumbtack staff to ensure high quality of service.
You're given a list of ratings for some Pros. Find out which Pros should be manually reviewed.
*Example:
For threshold = 3.5 and
ratings = [[3, 4],
           [3, 3, 3, 4],
           [4]]
the output should be ratingThreshold(threshold, ratings) = [1].
Assume that we have 3 Pros that have received the following ratings: [3, 4], [3, 3, 3, 4] and [4]. Then And if threshold = 3.5 the answer is ratingThreshold(threshold, ratings) = [1]. The first Pro's rating is 3.5, the second one's is 3.25, and the last one's is 4, so only the second Pro should be reviewed manually (the output is their 0-based index).
'''
def ratingThreshold(threshold, ratings):
    a, b = [], []
    for i in range(len(ratings)):
        a.append(sum(ratings[i])/len(ratings[i]))
        if a[i] < threshold:
            b.append(i)
    return b

'''
Thumbtack helps Professionals (Pros) grow their business by identifying new customers. Upon registering on Thumbtack, a Pro specifies which categories of services they provide. To help match customer requests with qualified Pros, Thumbtack maintains a list of Pros grouped by service categories.
Given a list of pros and their category preferences, return the list of Pros for each category.
*Example:
For pros = ["Jack", "Leon", "Maria"] and
preferences = [["Computer repair", "Handyman", "House cleaning"],
               ["Computer lessons", "Computer repair", "Data recovery service"],
               ["Computer lessons", "House cleaning"]]
the output should be
proCategorization(pros, preferences) = [[["Computer lessons"], ["Leon", "Maria"]],
                                        [["Computer repair"], ["Jack", "Leon"]],
                                        [["Data recovery service"], ["Leon"]],
                                        [["Handyman"], ["Jack"]],
'''                                    
def proCategorization(pros, preferences):

    a, out = len(preferences), []
    work = []
    for i in preferences:
        for j in range(len(i)):
            work.append(i[j])
    unique_work = sorted(list(set(work)))
    
    for i in unique_work:
        w = []
        for j in range(a):
            if i in preferences[j]:
                w.append(pros[j])
        out.append([[i], w])
    return out
                
'''
A Thumbtack customer has just submitted a request for a house painter to paint a one bedroom house in San Francisco. Our job is to find Pros who provide this service and whose travel distance preference is ideal for the job. To measure how well the Pro and the request match, we calculate their matching score and non-matching score as follows:
if the Pro's distance from the customer's house does not exceed their maximum preferred travel distance, then their matching score equals the distance between the pro and the customer;
otherwise we calculate a non-matching score as the difference between the distance from the pro to the customer, and their maximum preferred travel distance.
For example, let's say a pro Jane has a maximum travel distance of 10 miles.
If a customer is located 5 miles away, their matching score is 5 miles.
If a customer is located 12 miles away, their "non-matching" score is 2 miles.
To select the top 5 Pros, we sort them so that those who have a matching score are always shown before those who have a non-matching score, and both matching scores and non-matching scores are sorted in ascending order. If two or more Pros have equal scores, they are sorted by their names in lexicographical order.
You're given a list of pros who match the "house painting" category, their distances from the customer's house, and their travelPreferences, which denotes the maximum distance each Pro is willing to travel for a given job. Return the top 5 Pros sorted as described above. If there are fewer than 5 Pros, return them all.
*Example:
For
pros = ["Michael", "Mary", "Ann", "Nick", "Dan", "Mark"],
distances = [12, 10, 19, 15, 5, 20], and
travelPreferences = [12, 8, 25, 10, 3, 10], the output should be
requestMatching(pros, distances, travelPreferences) = ["Michael", "Ann", "Dan", "Mary", "Nick"].
Here's how Pros will be sorted in accordance with their scores:
"Michael": matching score equals 12;
"Ann": matching score equals 19;
"Dan": non-matching score equals 5 - 3 = 2;
"Mary": non-matching score equals 10 - 8 = 2;
"Nick": non-matching score equals 15 - 10 = 5;
"Mark": non-matching score equals 20 - 10 = 10.
For
pros = ["Ann", "Michael", "Mary"],
distances = [5, 5, 5], and
travelPreferences = [3, 10, 7], the output should be
requestMatching(pros, distances, travelPreferences) = ["Mary", "Michael", "Ann"].
'''
def requestMatching(pros, distances, travelPreferences):

    l1, l2 = {}, {}
    for i, j, k in zip(pros, distances, travelPreferences):
        if j <= k:
            l1[i] = j
        else:
            l2[i] = j - k
    l1 = [x[0] for x in sorted(l1.items(), key=lambda x: (x[1], x[0]))]
    l2 = [y[0] for y in sorted(l2.items(), key=lambda x: (x[1], x[0]))]
    return (l1+l2)[:5]

'''
When a customer submits a job request on Thumbtack, this information is sent to Pros in the area who might be interested in it. If it looks like there's a fit, a Pro can respond with a custom quote that includes a personal message and a price estimate.
Thumbtack tries to help Pros pick a price estimate range using historical contractData, which contains prices for the same job type in the same area. You have been asked to implement the following two-step price suggestion algorithm:
In the first step, contractData, which is guaranteed to have an even length, is sorted and divided into two groups:
the first group contains the first half of the elements in contractData.
the second group contains the other half;
In the second step, the median values of the first and the second groups are found:
the median of the first group is rounded down and returned as the lower price bound;
the median of the second group is rounded up and returned as the upper price bound.
If the data is insufficient (i.e. contractData contains fewer than 2 elements), a suggestion cannot be made, so nothing should be returned.
Using the given contractData, find the lower and the upper bounds of the suggested price estimate range.
*Example:
For contractData = [10, 15, 14, 7, 11, 15], the output should be priceSuggestion(contractData) = [10, 15].
The first step produces groups [7, 10, 11] and [14, 15, 15];
The second step returns 10 and 15.
For contractData = [], the output should be priceSuggestion(contractData) = [].
'''
def priceSuggestion(contractData):

    from math import ceil
    l = len(contractData)
    if l == 0:
        return []
    
    l1 = sorted(contractData)[:l//2]
    l2 = sorted(contractData)[l//2:]
    l_ = len(l1)
    if l_%2:
        return [l1[l_//2], l2[l_//2]]
    else:
        return [(l1[l_//2-1]+l1[l_//2])//2, ceil((l2[l_//2-1]+l2[l_//2])/2)]
