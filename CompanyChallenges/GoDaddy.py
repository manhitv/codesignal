'''
GoDaddy makes a lot of different top-level domains available to its customers. A top-level domain is one that goes directly after the last dot ('.') in the domain name, for example .com in example.com. To help the users choose from available domains, GoDaddy is introducing a new feature that shows the type of the chosen top-level domain. You have to implement this feature.
To begin with, you want to write a function that labels the domains as "commercial", "organization", "network" or "information" for .com, .org, .net or .info respectively.
For the given list of domains return the list of their labels.
*Example:
For domains = ["en.wiki.org", "codesignal.com", "happy.net", "code.info"], the output should be domainType(domains) = ["organization", "commercial", "network", "information"].
'''
def domainType(domains):
    a = []
    for i in range(len(domains)):
        ai = ''
        if domains[i][-4:] == '.com':
            ai = 'commercial'
        if domains[i][-4:] == '.org':
            ai = 'organization'
        if domains[i][-4:] == '.net':
            ai = 'network'
        if domains[i][-4:] == 'info':
            ai = 'information'
        a.append(ai)
    return a

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
GoDaddy’s Online Store product allows our small business customers to create ecommerce websites for selling products online. Let's assume you're a new intern who's been tasked with creating a frontend component for reordering products in a list via a simple drag-and-drop interface. For this exercise, we can assume that you are building the mobile UI, where you can only drag and drop items along the y-axis (i.e. vertically).
Your job is to implement a function that returns the 0-based index where the currently dragged element should be inserted once it is dropped. In the correct case it should be placed below all elements whose midpoints are above the current y position of the mouse.
Note that both y coordinates and elements' indices increase downwards.
*Example:
For boundaries = [0, 10, 50, 100, 120] and y = 45, the output should be reorderingOfProducts(boundaries, y) = 2.
The item with index 0 occupies points with y-coordinates from the interval [0, 10], the item with index 1 occupies points with y-coordinates from the interval [10, 50], etc. The bottommost item has index 3 and occupies points with y-coordinates from the interval [100, 120].
If y = 45 then the answer should be 2.
Midpoints for each of the static items are [5, 30, 75, 110], respectively. Thus, the currently dragged element will be inserted below the two topmost elements and above each of the other ones.
For boundaries = [0, 10, 50, 100, 120] and y = 110, the output should be reorderingOfProducts(boundaries, y) = 3.
Note that the dragged element should be placed above the bottommost element because the y-coordinate of the former equals the midpoint of the latter.
For boundaries = [0, 10, 50, 100, 120] and y = 111, the output should be reorderingOfProducts(boundaries, y) = 4.
'''
def reorderingOfProducts(boundaries, y):
    boundaries.insert(0, -float('inf'))
    l = 0
    r = len(boundaries) - 1
    while l + 1 < r:
        mid = (l + r) // 2
        if (boundaries[mid] + boundaries[mid+1])/2 < y:
            l = mid
        else:
            r = mid
    return l
