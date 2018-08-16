#anagram check

def anagram(s1, s2):
    
    s1Len = s2Len = 0
    s1Copy = []    
    s2Copy = []
    for i in range(len(s1)):
        if not s1[i].isspace():
            s1Len += 1
            s1Copy.append(s1[i].lower())
    for j in range(len(s2)):
        if not s2[j].isspace():
            s2Len += 1
            s2Copy.append(s2[j].lower())
    
    s1Copy.sort()
    s2Copy.sort()
    if s1Copy != s2Copy:
        return False
    return True

print(anagram('God', 'Dog'))
print(anagram('clint eastwood','old west action'))
print(anagram('good', 'god'))
print(anagram('clint eastwood', 'tld west action'))
