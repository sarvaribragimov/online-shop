# Performace counter

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start} seconds")
        return result

    return wrapper


# usage

# @timer
# def test():
#     li = []
#     for i in range(10_000_000):
#         li.append(i**10)
#     return li

# test()
