#array pair sum
def pairSum(arr, target):

    pairs = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                testPair = list((arr[i], arr[j]))
                if testPair not in pairs and testPair.reverse() not in pairs:
                    pairs.append(testPair)
    print(pairs)
    return len(pairs)

print(pairSum([3,1,2,2], 4))
print(pairSum([2,7,8,3,5,5,6,4,1], 10))
