'''
When migrating data from a source storage system to a target storage system, the number one focus is avoiding data corruption at all cost. In order to meet these high standards, various rounds of tests are run checking for corrupted blocks as well as successfully migrated lengthy regions.
We are going to represent the source storage system and target storage system as sequential arrays sourceArray and destinationArray respectively, where sourceArray[i] represents binary data of the ith source block as an integer, and destinationArray[i] represents binary data of the ith destination block, where the data should be migrated, also as an integer. Given the content of the source and the migrated content of the target, find the length and the starting block of the longest uncorrupted data segment (segment = subsequent blocks).
If there is no uncorrupted segment, return an array containing 0 and 0 respectively.
*Example:
For sourceArray = [33531593, 96933415, 28506400, 39457872, 29684716, 86010806] and destinationArray = [33531593, 96913415, 28506400, 39457872, 29684716, 86010806], the output should be longestUncorruptedSegment(sourceArray, destinationArray) = [4, 2].
The only corrupted element is located by index 1, where sourceArray[1] = 96933415 != 96913415 = destinationArray[1], all other data blocks were transfered uncorrupted. So the longest uncorrupted segment starts on second index and goes to the end of the array, thus having length 4.
'''
def longestUncorruptedSegment(sourceArray, destinationArray):

    a = zip(sourceArray,destinationArray )
    res = []
    for i, e in enumerate(a):
        if e[0] == e[1]:
            res.append(0)
        else:
            res.append(1)
    
    res_start, res_len = 0, 0
    lenn = 0
    first = True
    prev = 0
    start = 0
    for i in range(len(res)):
        if res[i] == 1:
            lenn = 0
        else:
            lenn += 1
            if prev != 0 or i==0:
                start = i 
            if res_len < lenn:
                res_len = lenn
                res_start = start
        prev = res[i]
                      
    return [res_len, res_start]
    
