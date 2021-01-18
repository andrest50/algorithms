import sys
import random

def selectionSort(A):
    for i in range(len(A)):
        minInt = sys.maxsize
        minIndex = 0
        for j in range(i, len(A)):
            if(A[j] < minInt):
                minInt = A[j]
                minIndex = j
        A[minIndex] = A[i]
        A[i] = minInt

def getNumbers(numbers, length):
    for i in range(length):
        numbers.append(random.randrange(1, 100))

def main():
    numbers = []
    getNumbers(numbers, 20)
    print("Before: {}".format(numbers))
    selectionSort(numbers)
    print("After: {}".format(numbers))

main()