import random

def binarySearch(numbers, search, left, right):
    mid = int((left + right) / 2)
    print("Left: {}, Right: {}, Mid: {}".format(left, right, mid))
    if(numbers[mid] == search):
        return mid
    elif(left >= right):
        return -1
    elif(numbers[mid] < search):
        return binarySearch(numbers, search, mid+1, right)
    else:
        return binarySearch(numbers, search, left, mid-1)

def getNumbers(numbers, length):
    for i in range(length):
        numbers.append(random.randrange(1, 100))

def main():
    numbers = []
    getNumbers(numbers, 20)
    numbers.sort()
    search = random.randrange(1, 100)
    index = binarySearch(numbers, search, 0, len(numbers)-1)
    print("List: {}".format(numbers))
    print("Index of value {} if found: {}".format(search, index))

main()