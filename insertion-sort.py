import sys
import random

def insertionSort(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if(A[j] > A[j+1]):
                temp = A[j+1]
                A[j+1] = A[j]
                A[j] = temp

def getNumbers(numbers, length):
    for i in range(length):
        numbers.append(random.randrange(1, 100))

def main():
    numbers = []
    getNumbers(numbers, 20)
    print("Before: {}".format(numbers))
    insertionSort(numbers)
    print("After: {}".format(numbers))

main()