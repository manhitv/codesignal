'''
Instacart customers are able to set the delivery window during which they want to receive their groceries. There are always plenty of shoppers in the area ready to take a customer's order, but unfortunately they can't always do it right away. Before taking an order a shopper wants to ensure they will make it in time. They also don't want to stay idle, so arriving early isn't an option either.
Our task is to implement an algorithm that determines whether shoppers should take the given order or not.
For each shopper you know their travel speed, distance to the store and the estimated amount of time they will spend there. Figure out which of them can take the order, assuming it is known when the customer wants to receive the groceries and the distance between their house and the store.
*Example:
For order = [200, 20, 15] and shoppers = [[300, 40, 5], [600, 40, 10]], the output should be
delivery(order, shoppers) = [false, true].
The store is located 200 m away from the customer's house.
The customer will be ready to receive the groceries in 20 minutes, but they shouldn't be delivered more than 15 minutes late.
The first shopper is 300 m away from the store, his speed is 40 m/min, and he will spend 5 minutes in the store, which means that he will need (300 + 200) / 40 + 5 = 17.5 minutes to fulfill the order. This will leave him with 20 - 17.5 = 2.5 idle minutes, so he shouldn't take the order.
The second shopper is 600 m away from the store, his speed is 40 m/min, and he will spend 10 minutes in the store, which means it will take him (600 + 200) / 40 + 10 = 30 minutes to fulfill the order. The customer can wait for 20 + 15 = 35 minutes, which means that the shopper will make it in time.
'''
def delivery(order, shoppers):
    t_fulfill = []
    out = []
    for i in range(len(shoppers)):
        t_fulfill.append((shoppers[i][0] + order[0])/shoppers[i][1] + shoppers[i][2])
        if t_fulfill[i] < order[1] or t_fulfill[i] > order[1] + order[2]:
            out.append(False)
        else:
            out.append(True)
    return out

'''
As part of an Instacart beta testing group, Sara is trying out a brand new feature that automatically estimates the combined cost of the items in her handwritten shopping list. Her list contains both items and their prices. All Sara has to do is snap a photo of her list with the Instacart app, and she gets a quick estimate of what everything will cost.
Sara asked for your help, so it is up to you to devise an algorithm that calculates the cost after the image is converted into plain text. All you need to do is extract all numbers from the given string items and sum them up.
*Example:
For items = "Doughnuts, 4; doughnuts holes, 0.08; glue, 3.4", the output should be shoppingList(items) = 7.48;
For items = "blue suit for 24$, cape for 12.99$ & glasses for 15.70", the output should be shoppingList(items) = 52.69.
'''
def shoppingList(items):

    import re
    s = re.findall(r"\d+\.\d+|\d+", items)
    return sum([float(i) for i in s])
