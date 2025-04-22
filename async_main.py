import asyncio
import functools


def printing_decorator(func):
    @functools.wraps(func)
    async def wrapper(*arg, **kwargs):
        print("Before function call")
        result = await func(*arg, **kwargs)
        print("After function call")
        print(result)
        return result
    return wrapper

@printing_decorator
def print_hello():
    print("Hello")

@printing_decorator
async def print_hello_async():
    print("Hello")
    return 1

if __name__ == "__main__":
    asyncio.run(print_hello_async())