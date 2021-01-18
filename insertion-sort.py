import sys

def insertionSort(A):
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if(A[j] > A[j+1]):
                temp = A[j+1]
                A[j+1] = A[j]
                A[j] = temp


def main():
    numbers = [4, 2, 3, 1, -3, 7, 5, 9]
    print("Before: {}".format(numbers))
    insertionSort(numbers)
    print("After: {}".format(numbers))

main()