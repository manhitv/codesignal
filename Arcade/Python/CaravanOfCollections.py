'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You need to compress a large document that consists of a small number of different characters. To choose the best encoding algorithm, you would like to look closely at the characters that comprise this document.
Given a document, return an array of all unique characters that appear in it sorted by their ASCII codes.
*Example:
For document = "Todd told Tom to trot to the timber", the output should be uniqueCharacters(document) = [' ', 'T', 'b', 'd', 'e', 'h', 'i', 'l', 'm', 'o', 'r', 't'].
'''
def uniqueCharacters(document):
    return sorted(set(document))

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
For the upcoming academic year the Coolcoders University should decide which students will get the scholarships. Scholarships are considered to be correctly distributed if all best students have it, but not all students in the university do. Obviously, only university students should be able to get a scholarship, i.e. there should be no outsiders in the list of the students that will get a scholarships.
You are given lists of unique student ids bestStudents, scholarships and allStudents, representing ids of the best students, students that will get a scholarship and all the students in the university, respectively. Return true if the scholarships are correctly distributed and false otherwise.
*Example:
For bestStudents = [3, 5], scholarships = [3, 5, 7], and allStudents = [1, 2, 3, 4, 5, 6, 7], the output should be correctScholarships(bestStudents, scholarships, allStudents) = true;
For bestStudents = [3, 5], scholarships = [3, 5], and allStudents = [3, 5], the output should be
correctScholarships(bestStudents, scholarships, allStudents) = false.
All students get a scholarship, which is not correct.
For bestStudents = [3], scholarships = [1, 3, 5], and allStudents = [1, 2, 3], the output should be
correctScholarships(bestStudents, scholarships, allStudents) = false.
There's no student with id 5, yet somehow he managed to get a scholarship.
'''
def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You decided to found your own startup company and now want to choose a proper name for it. There are three large companies that you want to compete against, and since their names are quite popular you want to use their names as a starting point. You want to use only popular characters in the name of your company, but not too mainstream. You consider a character to be popular if it appears in at least two company names, and consider it to be mainstream if it appears in all three.
Given the names of the companies, return the list of characters that are popular but not mainstream sorted by their ASCII codes.
*Example:
For companies = ["coolcompany", "nicecompany", "legendarycompany"], the output should be startupName(companies) = ['e', 'l'].
Here's how the answer can be obtained:
these letters appear in all three company names and are thus mainstream: 'a', 'c', 'm', 'n', 'o', 'p', 'y';
these letters appear only in one of the company names and are thus not popular: 'd', 'g', 'i', 'r';
the remaining letters are popular and not mainstream: 'e', 'l'.
'''
def startupName(companies):
    cmp1 = set(companies[0])
    cmp2 = set(companies[1])
    cmp3 = set(companies[2])
    res = (cmp1 & cmp2 | cmp1 & cmp3 | cmp2 & cmp3) - (cmp1 & cmp2 & cmp3)
    return list(sorted(list(res)))

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You are working on an AI that can recognize words. To begin with, you'd like to try the following approach: for the given pair of words the AI should find two strings of sorted letters that uniquely identify these words.
Given words word1 and word2, return an array of two strings sorted lexicographically, where the first string contains characters present only in word1, and the second string contains characters present only in word2.
*Example:
For word1 = "program" and word2 = "develop", the output should be wordsRecognition(word1, word2) = ["agmr", "delv"].
Letters 'o' and 'p' are present in both words, and other letters identify them uniquely.
'''
def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        return ''.join(sorted(list(set(w1) - set(w2))))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You're implementing a plugin for your favorite code editor. This plugin launches various scripts depending on the open file extension. Each script is associated with exactly one extension, and the information about which script should be launched for each extension is stored in a dictionary scriptByExtension.
You are planning to add more supported extensions for some scripts, so now you would also like to store information about the extensions which each script supports. As a starting point, you'd like to obtain the (extension, script) pairs from the dictionary, sorted lexicographically by the extensions.
Implement a function that will do the job.
*Example:
For
scriptByExtension = {
  "validate": "py",
  "getLimits": "md",
  "generateOutputs": "json"
}
the output should be
transposeDictionary(scriptByExtension) = [["json", "generateOutputs"], 
                                          ["md", "getLimits"], 
                                          ["py", "validate"]]
'''
def transposeDictionary(scriptByExtension):
    return sorted([[value, key] for key, value in scriptByExtension.items()])

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
Your friend has been doodling during the lecture and wrote down several digits in a circle. You're wondering if these digits might form the password to your friend's computer. You're planning to prank him some time in the future, and hacking into his computer will definitely help. If the digits written in the clockwise order indeed form a password, all you need to do is figure out which digit comes in it first.
Given a list of digits as they are written in the clockwise order, find all other combinations the password could possibly have.
*Example:
For digits = [1, 2, 3, 4, 5], the output should be
doodledPassword(digits) = [[1, 2, 3, 4, 5], [2, 3, 4, 5, 1], [3, 4, 5, 1, 2],
                           [4, 5, 1, 2, 3], [5, 1, 2, 3, 4]]
'''
from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x,y: x.rotate(y), res, range(n,0,-1)), 0)
    return [list(d) for d in res]

'''
Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
You've recently read "The Gold-Bug" by Edgar Allan Poe, and was so impressed by the cryptogram in it that decided to try and decipher an encrypted text yourself. You asked your friend to encode a piece of text using a substitution cipher, and now have an encryptedText that you'd like to decipher.
The encryption process in the story you read involves frequency analysis: it is known that letter 'e' is the most frequent one in the English language, so it's pretty safe to assume that the most common character in the encryptedText stands for 'e'. To begin with, implement a function that will find the most frequent character in the given encryptedText.
*Example:
For encryptedText = "$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ", the output should be frequencyAnalysis(encryptedText) = 'C'.
Letter 'C' appears in the text more than any other character (4 times), which is why it is the answer.
'''
from collections import Counter

def frequencyAnalysis(encryptedText):
    return Counter(encryptedText).most_common(1)[0][0]
