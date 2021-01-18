import sys
import random

minimum = sys.maxsize
maximum = 0

def minAndMax(A, left, right):
    global minimum, maximum
    mid = int((left + right) / 2)
    if(left > right):
        return
    if(A[mid] > maximum):
        maximum = A[mid]
    if(A[mid] < minimum):
        minimum = A[mid]
    minAndMax(A, left, mid-1)
    minAndMax(A, mid+1, right)
    return

def getNumbers(numbers, length):
    for i in range(length):
        numbers.append(random.randrange(0, 100))

def main():
    numbers = []
    getNumbers(numbers, 20)
    minAndMax(numbers, 0, len(numbers)-1)
    print("List: {}".format(numbers))
    print("Min: {}, Max: {}".format(minimum, maximum))

main()