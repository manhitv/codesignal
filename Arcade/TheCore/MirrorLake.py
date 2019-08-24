'''
Given two strings a and b, both consisting only of lowercase English letters, your task is to calculate how many strings equal to a can be constructed using only letters from the string b? Each letter can be used only once and in one string only.
*Example:
For a = "abc" and b = "abccba", the output should be stringsConstruction(a, b) = 2.
We can construct 2 strings a = "abc" using only letters from the string b.
For a = "ab" and b = "abcbcb", the output should be stringsConstruction(a, b) = 1.
'''
def stringsConstruction(a, b):
    d, e, f = [], [], []
    for ele in a:
        if ele not in e:
            e.append(ele)
    for i in range(len(e)):
        f.append(a.count(e[i]))
    for i in range(len(e)):
        c = 0
        for j in range(len(b)):
            if e[i] == b[j]:
                c += 1
        d.append(c//f[i])
    return min(d)
            
'''            
A ciphertext alphabet is obtained from the plaintext alphabet by means of rearranging some characters. For example "bacdef...xyz" will be a simple ciphertext alphabet where a and b are rearranged.
A substitution cipher is a method of encoding where each letter of the plaintext alphabet is replaced with the corresponding (i.e. having the same index) letter of some ciphertext alphabet.
Given two strings, check whether it is possible to obtain them from each other using some (possibly, different) substitution ciphers.
*Example:
For string1 = "aacb" and string2 = "aabc", the output should be isSubstitutionCipher(string1, string2) = true.
Any ciphertext alphabet that starts with acb... would make this transformation possible.
For string1 = "aa" and string2 = "bc", the output should be isSubstitutionCipher(string1, string2) = false.
'''
def isSubstitutionCipher(string1, string2):
    d, r = {}, {}
    for x,y in zip(string1,string2):
        if x not in d:
            d[x] = y
        elif d[x]!= y:
            return False
        
        if y not in r:
            r[y] = x
        elif r[y]!= x:
            return False
    return True
