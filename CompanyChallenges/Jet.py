'''
Before delivery, all orders at Jet are packed into boxes to protect them from damage.
Consider a package pkg of a given size that needs to be packed into a box chosen from a list of available boxes. The package should fit inside the box, keeping in mind that the size of the package should not exceed the size of the box in any dimension (note that the package can be rotated to fit and it can be positioned upside down). For the sake of efficiency, among the available boxes that fit, the one with smallest volume should be chosen.
Given a package pkg and available boxes, find the 0-based index of the smallest-by-volume box such that the package fits inside it, or return -1 if there is no such box.
*Example:
For pkg = [4, 2, 5] and boxes = [[4, 3, 5], [5, 2, 5]], the output should be packageBoxing(pkg, boxes) = 1.
The package fits into both boxes, but the volume of the first one (4 * 3 * 5 = 60) is greater than the volume of the second (5 * 5 * 2 = 50).
For pkg = [4, 4, 2] and boxes = [[2, 4, 4], [4, 4, 3]], the output should be packageBoxing(pkg, boxes) = 0.
The package can fit into the first box if it is rotated, and into the second box as-is, but the first box is chosen because it has less volume overall.
For pkg = [4, 5, 3] and boxes = [[3, 10, 2], [2, 6, 7], [1, 1, 1]], the output should be packageBoxing(pkg, boxes) = -1.
The package doesn't fit into any of the available boxes.
'''
def packageBoxing(pkg, boxes):

    import math
    pkg, min_v, index = sorted(pkg), math.inf, 0
    for i in range(len(boxes)):
        if all(m <= n for m, n in zip(pkg, sorted(boxes[i]))):
            a = boxes[i][0]*boxes[i][1]*boxes[i][2]
            if min_v > a:
                min_v = a
                index = i
    return index if min_v != math.inf else -1 
            
'''
Jet.com customers can easily find the item they are looking for by browsing by category. Categories are stored in a catalog that is updated on a regular basis as inventory changes. Your goal is to implement an algorithm that updates the catalog with new items.
The catalog is given as a two-dimensional array. For each i, catalog[i][0] represents the name of the corresponding category, and catalog[i][j] for j > 0 is the name of some item within this category, which can also be the category of some other items. For each i all elements of catalog[i] except the first are sorted lexicographically, and catalog arrays are sorted lexicographically by their first elements. The name of the topmost directory is "root".
Given a list of updates, update the catalog with the new items and return the result.
*Example:
For
catalog = [["Books", "Classics", "Fiction"],
           ["Electronics", "Cell Phones", "Computers", "Ultimate item"],
           ["Grocery", "Beverages", "Snacks"],
           ["Snacks", "Chocolate", "Sweets"],
           ["root", "Books", "Electronics", "Grocery"]]
and
updates = [["Snacks", "Marmalade"],
           ["Fiction", "Harry Potter"],
           ["root", "T-shirts"],
           ["T-shirts", "CodeSignal"]]
the output should be
catalogUpdate(catalog, updates) = [["Books", "Classics", "Fiction"],
                                   ["Electronics", "Cell Phones", "Computers", "Ultimate item"],
                                   ["Fiction", "Harry Potter"],
                                   ["Grocery", "Beverages", "Snacks"],
                                   ["Snacks", "Chocolate", "Marmalade", "Sweets"],
                                   ["T-shirts", "CodeSignal"],
                                   ["root", "Books", "Electronics", "Grocery", "T-shirts"]]
'''
def catalogUpdate(catalog, updates):

    d = {}
    for cat in catalog:
        d[cat[0]]=cat[1:]
    for cat in updates:
        if cat[0] in d.keys():
            d[cat[0]]+=cat[1:]
        else:
            d[cat[0]] = cat[1:]
    final_catalog = []
    for cat in sorted(d.keys()):
        temp_list = [cat]
        temp_list+=sorted(d[cat])
        final_catalog.append(temp_list)
    return final_catalog
                
