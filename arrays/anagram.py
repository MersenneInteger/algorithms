#anagram check

def anagram(s1, s2):
    
    s1Len = s2Len = 0
    for i in range(len(s1)):
        if not s1[i].isspace():
            s1Len += 1
    for i in range(len(s2)):
        if not s2[i].isspace():
            s2Len += 1
    if s1Len != s2Len:
        return False
    for i in range(s1Len):
        if s2[i].lower() not in s1.lower():
            return False
    return True

print(anagram('God', 'Dog'))
print(anagram('penis','spine'))
print(anagram('clint eastwood','old west action'))
print(anagram('python', 'javascript'))
