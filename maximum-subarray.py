import sys
import random

def findMaxCrossingSubarray(A, low, mid, high):
    leftSum = -sys.maxsize
    total = 0
    maxLeft = 0
    for i in range(mid, low, -1):
        total += A[i]
        if(total > leftSum):
            leftSum = total
            maxLeft = i
    rightSum = -sys.maxsize
    total = 0
    maxRight = 0
    for j in range(mid+1, high):
        total += A[j]
        if(total > rightSum):
            rightSum = total
            maxRight = j
    return (maxLeft, maxRight, leftSum + rightSum)

def findMaximumSubarray(A, low, high):
    if(high == low):
        return (low, high, A[low])
    else:
        mid = int((low + high) / 2)
        (leftLow, leftHigh, leftSum) = findMaximumSubarray(A, low, mid)
        (rightLow, rightHigh, rightSum) = findMaximumSubarray(A, mid+1, high)
        (crossLow, crossHigh, crossSum) = findMaxCrossingSubarray(A, low, mid, high)
        if(leftSum >= rightSum and leftSum >= crossSum):
            return (leftLow, leftHigh, leftSum)
        elif(rightSum >= leftSum and rightSum >= crossSum):
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)

def getNumbers(numbers, length):
    for i in range(length):
        numbers.append(random.randrange(-50, 50))

def main():
    numbers = []
    getNumbers(numbers, 20)
    (low, high, total) = findMaximumSubarray(numbers, 0, len(numbers)-1)
    print("List: {}".format(numbers))
    print("Low: {}, High: {}, Sum: {}".format(low, high, total))

main()