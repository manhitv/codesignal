'''
Check if the given string is a correct time representation of the 24-hour clock.
*Example:
For time = "13:58", the output should be validTime(time) = true;
For time = "25:51", the output should be validTime(time) = false;
For time = "02:76", the output should be validTime(time) = false.
'''
def validTime(time):

    hours, minutes = int(time[:2]), int(time[3:])
    return 0 <= hours <= 23 and 0 <= minutes <= 59

'''
You have been watching a video for some time. Knowing the total video duration find out what portion of the video you have already watched.
*Example:
For part = "02:20:00" and total = "07:00:00", the output should be videoPart(part, total) = [1, 3].
You have watched 1 / 3 of the whole video.
'''
def videoPart(part, total):
    import math
    p, t = [int(i) for i in part.split(':')], [int(j) for j in total.split(':')]
    dominator, numerator = p[0]*3600+p[1]*60+p[2], t[0]*3600 + t[1]*60 + t[2]
    gcd = math.gcd(dominator, numerator)
    return [dominator//gcd, numerator//gcd]

