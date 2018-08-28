import collections

#find the missing element
def finder(arr1, arr2):

    arr1Map = {}
    arr2Map = {}
    maxLen = (max(arr1) if max(arr1) > max(arr2) else max(arr2))+1
    for i in range(maxLen):
        arr1Map.setdefault(i, 0)
        arr2Map.setdefault(i, 0)
    for i in arr1:
        arr1Map[i] = arr1Map.get(i) + 1
    for i in arr2:
        arr2Map[i] = arr2Map.get(i) + 1
    for i in range(maxLen):
        if arr1Map.get(i) != 0 and arr1Map.get(i) != arr2Map.get(i):
            return i

print(finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]))
print(finder([5,5,7,7], [5,5,7]))
print(finder([10,3,3,1,1], [10, 3, 1, 1]))

def finder2(arr1, arr2):
    
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
    return arr1[-1]

print(finder([1,2,3], [1,3]))

#using hash tables
def finder3(arr1, arr2):

    d = collections.defaultdict(int)
    for num in arr2:
        d[num] += 1
    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1

print(finder3([5,5,7,7], [5,5,7]))
print('-' * 10)

def finder4(arr1, arr2):

    result = 0
    for num in arr1 + arr2:
        result ^= num
        print(result)
    print('missing elem: {}'.format(result))

finder4([5,5,7,7], [5,5,7])
