myArray = [2, 3, 6, 9, 12, 15, 19]

def search(elm,low,high, myArray):
    while(low <= high):
        mid = (low + high) // 2
        if myArray[mid] == elm:
            return "elm " + str(elm) + " found at index " + str(mid) + "!!!"
        elif myArray[mid] > elm:
            print("elm " + str(elm) + " less than index " + str(mid) + " value " + str(myArray[mid]))
            high = mid - 1
        else:
            print("elm " + str(elm) + " greater than index " + str(mid) + " value " + str(myArray[mid]))
            low = mid + 1

    return "elm not found"
print(search(12, 0, 6, myArray))
