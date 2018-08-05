#anagram check

def anagram(s1, s2):
    
    s1Len = s2Len = 0
    s1Copy = s2Copy = []    
    for i in range(len(s1)):
        if not s1[i].isspace():
            s1Len += 1
            s1Copy.append(s1[i].lower())
    for i in range(len(s2)):
        if not s2[i].isspace():
            s2Len += 1
            s2Copy.append(s2[i].lower())
    if s1Len != s2Len:
        return False
    charChecker = [0] * s1Len
    for i in range(s1Len):
        if s2Copy[i] not in s1Copy:
            return False
        for j in range(s2Len):
            if s2Copy[i] == s1Copy[i]:
                charChecker[i] += 1
    for i in range(len(charChecker)):
        if charChecker[i] % 2 != 0:
            return False
    return True

print(anagram('God', 'Dog'))
print(anagram('penis','spine'))
print(anagram('clint eastwood','old west action'))
print(anagram('python', 'javascript'))
print(anagram('good', 'god'))
print(anagram('clint eastwood', 'tld west action'))
