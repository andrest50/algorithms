def binarySearch(numbers, search, left, right):
    mid = int((left + right) / 2)
    #print("Left: {}, Right: {}, Mid: {}".format(left, right, mid))
    if(numbers[mid] == search):
        return mid
    elif(left >= right):
        return -1
    elif(numbers[mid] < search):
        return binarySearch(numbers, search, mid+1, right)
    else:
        return binarySearch(numbers, search, left, mid-1)


def main():
    numbers = [1, 2, 4, 6, 7, 9, 11, 13]
    search = 9
    index = binarySearch(numbers, search, 0, len(numbers)-1)
    print("Index: {}".format(index))

main()