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
    if s1Len != s2Len:
        return False

    s1Copy.sort()
    s2Copy.sort()
    if s1Copy != s2Copy:
        return False
    return True

print(anagram('God', 'Dog'))
print(anagram('clint eastwood','old west action'))
print(anagram('good', 'god'))
print(anagram('clint eastwood', 'tld west action'))

def ezAnagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

print(anagram('Tom Marvolo Riddle', 'I am Lord Voldemort'))

def otherAnagram(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False
    count = {}
    for letter in s1:
        if letter not in count:
            count[letter] = 1
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    for k in count:
        if count[k] != 0:
            return False
    return True

print(anagram('Ggod', 'dgog'))
