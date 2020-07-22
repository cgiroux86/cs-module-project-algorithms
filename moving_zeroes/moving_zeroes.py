'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr, idx=1):
    # i = 0
    # while i < len(arr)-1:
    #     print('in loop', arr[i], arr[i + 1])
    #     if arr[i] == 0:
    #         print(arr[i])
    #         p = arr[i]
    #         arr[i] = arr[i + 1]
    #         arr[i + 1] = p
    #         print(arr[i + 1], 'i+1', arr[i])
    #         i += 1
    # print(arr)
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        while j <= len(arr) - 1:
            if arr[i] == 0 and arr[j] != 0:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1
            j += 1
        i += 1
    print(arr)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
