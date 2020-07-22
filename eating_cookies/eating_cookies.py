'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


def memoize(func):
    cache = dict()

    def memoized_cookies(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_cookies


cookies = memoize(eating_cookies)

# print(cookies(30))

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
