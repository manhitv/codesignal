'''
One Very Important User (VIU) has a Very Confidential Document (VCD) stored on his Dropbox account. He doesn't let anyone see the VCD, especially his roommates who often have access to his devices.
Opening the Dropbox mobile app on the VIU's tablet requires a four-digit passcode. To ensure the confidentiality of the stored information, the device is locked out of Dropbox after 10 consecutive failed passcode attempts. We need to implement a function that given an array of attempts made throughout the day and the correct passcode checks to see if the device should be locked, i.e. 10 or more consecutive failed passcode attempts were made.
*Example:
For
passcode = "1111" and
attempts = ["1111", "4444",
            "9999", "3333",
            "8888", "2222",
            "7777", "0000",
            "6666", "7285",
            "5555", "1111"]
the output should be incorrectPasscodeAttempts(passcode, attempts) = true.
The first attempt is correct, so the user must have successfully logged in. However, the next 10 consecutive attempts are incorrect, so the device should be locked. Thus, the output should be true.
For
passcode = "1234" and
attempts = ["9999", "9999",
            "9999", "9999",
            "9999", "9999",
            "9999", "9999",
            "9999", "1234",
            "9999", "9999"]
the output should be incorrectPasscodeAttempts(passcode, attempts) = false.
There are only 9 consecutive incorrect attempts, so there's no need to lock the device.
'''
def incorrectPasscodeAttempts(passcode, attempts):
    cnt = 0
    for a in attempts:
        failed = False
        if a!=passcode:
            cnt+=1
            failed = True
        if cnt == 10:
            return True
        if not failed:
            cnt =0
    return False

'''
Dropbox holds a competition between schools called CampusCup. If you verify an email address from a college, university, or higher education institution, you earn 20 points toward your school's overall ranking. When a school receives at least 100 points, all of its registered members receive an additional 3 Gb of bonus space each. When the school receives at least 200 points, its registered members receive an additional 8 Gb. If the school receives at least 300 points, its members receive an additional 15 Gb. And finally, when a school receives at least 500 points, members receive an additional 25 Gb each.
You are given n registered emails, all of them unique. Each email has the following format: "<name>@<domain>", where <name> and <domain> are non-empty strings consisting of lowercase letters and a '.'. Identical domains correspond to the same school and vice versa.
Your task is to make a scoreboard, i.e. to sort the schools according to the amount of bonus space they each received (per student not in total). School A must be higher in the standings than school B if A received more space than B, or if they received equal number of gigabytes but the domain string of school A is lexicographically smaller than the one of school B.
*Example:
For emails = ["john.doe@mit.edu", "admin@rain.ifmo.ru", "noname@mit.edu"], the output should be campusCup(emails) = ["mit.edu", "rain.ifmo.ru"].
"mit.edu" scored 40 points, and "rain.ifmo.ru" just 20. Both universities got no additional space, so "mit.edu" must be higher in the standings because it is lexicographically smaller than "rain.ifmo.ru".
For
emails = ["b@harvard.edu", "c@harvard.edu", "d@harvard.edu", 
          "e@harvard.edu", "f@harvard.edu",
          "a@student.spbu.ru", "b@student.spbu.ru", "c@student.spbu.ru", 
          "d@student.spbu.ru", "e@student.spbu.ru", "f@student.spbu.ru", 
          "g@student.spbu.ru"]
the output should be campusCup(emails) = ["harvard.edu", "student.spbu.ru"].
"harvard.edu" - 100 points, 3 Gb of additional space.
"student.spbu.ru" - 140 points, also 3 Gb of additional space.
"harvard.edu" must be higher in the standings because it is lexicographically smaller than "student.spbu.ru".
For
emails = ["a@rain.ifmo.ru", "b@rain.ifmo.ru", "c@rain.ifmo.ru", 
          "d@rain.ifmo.ru", "e@rain.ifmo.ru", "noname@mit.edu"]
the output should be campusCup(emails) = ["rain.ifmo.ru", "mit.edu"].
"mit.edu" - 20 points, no additional space.
"rain.ifmo.ru" - 100 points, 3 Gb of additional space.
Therefore, "rain.ifmo.ru" must be higher in the standings.
'''
def campusCup(emails):

    list_email = [i.split('@')[1] for i in emails]
    set_email = {}
    for i in set(list_email):
        a = list_email.count(i)
        if a < 5:
            set_email[i] = 0
        elif 10 > a >= 5:
            set_email[i] = 3
        elif 15 > a >= 10:
            set_email[i] = 8
        elif 25 > a >= 15:
            set_email[i] = 15
        else:
            set_email[i] = 25
    return [x[0] for x in sorted(set_email.items(), key=lambda x:(-x[1], x[0]))]
