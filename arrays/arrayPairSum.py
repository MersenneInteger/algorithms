#array pair sum

def pairSum(arr, target):

    pairs = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                testPair = list((arr[i], arr[j]))
                if testPair not in pairs and testPair.reverse() not in pairs:
                    pairs.append(testPair)
    return pairs

print(pairSum([3,1,2,2], 4))
print(pairSum([2,7,8,3,5,5,6,4,1], 10))

def pair_sum(arr, k):

    if len(arr) > 2:
        return
    seen = set()
    unseen = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))
    #return len(output)
    print('\n'.join(map(str, list(output))))

pair_sum([1,3,2,2], 4)
