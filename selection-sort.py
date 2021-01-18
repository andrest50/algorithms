import sys

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


def main():
    numbers = [4, 2, 3, 1, -3, 7, 5, 9]
    print("Before: {}".format(numbers))
    selectionSort(numbers)
    print("After: {}".format(numbers))

main()