def findCountOfSmallerAfterSelf(array):
    length = len(array)
    resultArray = [0] * length

    for i in range(length):
        for j in range(i, length):
            if array[i] > array[j]:
                resultArray[i] += 1

    return resultArray


if __name__ == "__main__":
    nums = list(map(int, input().strip('[').strip(']').split(',')))

    print(findCountOfSmallerAfterSelf(nums))
