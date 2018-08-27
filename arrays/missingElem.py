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
