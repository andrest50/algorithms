import sys

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

def main():
    numbers = [2, 1, 9, 7, 3, 6, 0, 2, 3]
    minAndMax(numbers, 0, len(numbers)-1)
    print("Min: {}, Max: {}".format(minimum, maximum))

main()