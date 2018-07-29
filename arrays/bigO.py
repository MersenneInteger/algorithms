#big O examples

#O(1) Constant
def constantFunc(values):
    print(values[0])
#time complexity is constant bc it is only printing
#out the first index, regardless of input size
constantFunc([1,2,3])
constantFunc(range(1, 101))

#O(n) Linear
def linearFunc(lst):
    for val in lst:
        print(val)
#time complexity scales linearly with n
linearFunc(range(1,10))
linearFunc(range(1, 1000))
#the second function call with take 100x longer to exe

#O(n^2) Quadratic
def quadraticFunc(lst):
    for item1 in lst:
        for item2 in lst:
            print(item1, item2)
#time complexity scales n * n

#linear example O(2n)
def printTwice(lst):
    for val in lst:
        print(val)
    for val in lst:
        print(val)
printTwice([2,3,5,7])

def comp(lst):
    print(lst[0])           #0(1)
    midpoint = int(len(lst)/2)        #O(n/2) or O((1/2) * n)
    for val in lst[:midpoint]:
        print(val)
    for i in range(1,10):      #O(10)
        print('Hello World')
comp([1,2,3,4])
# O(1 + n/2 + 10) but the numbers become insignificant as n -> oo
#therefore function is O(n)

def matcher(lst, match):
    for item in lst:
        if item == match:
            return True
    return False

print(matcher(range(1,10), 1)) #O(1) bc 1 is first index (best case)
print(matcher(range(1,10), 11)) #O(n) bc every element has to be iterated through (worst case)

#space complexity example
def createlist(n):
    newList = []

    for num in range(n):
        newList.append(num)
    return newList

createList(5) #space complexity scales with input, is O(n)

def printer(n):
    for i in range(1, 10):
        print('Hello world')
#has constant space complexity O(1) but time complexity is O(n)

