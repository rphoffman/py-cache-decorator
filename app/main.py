from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memo = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Since arguments are immutable, args can be used as a cache key directly
        if args in memo:
            print("Getting from cache")
            return memo[args]
        
        print("Calculating new result")
        result = func(*args, **kwargs)
        memo[args] = result
        return result

    return wrapper