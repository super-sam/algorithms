def timetaken(fn):
    def wrapper(*args, **kwargs):
        from time import time
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"Time Taken: {end - start} sec")
        return result
    return wrapper