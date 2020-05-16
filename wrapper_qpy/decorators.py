from functools import wraps
import inspect


def static_vars(**kwargs):
    """
    Some functions should remember static variables.
    This decorator helps us remember them
    """
    def decorate(func):
        for arg in kwargs:
            setattr(func, arg, kwargs[arg])
        return func
    return decorate


def va_args(func):
    """
    A lot of console and logging functions have va_args
    to handle printing, by using this decorator we can simplify
    writing these functions
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        format_string = args[0]
        other_args = args[1:]
        string = format_string % other_args
        result = func(string)
        return result
    return wrapper


def va_args2(num_args):
    """
    Same as up, but sometimes format string comes after other arguments
    @va_args2(0) is same as @va_args
    """
    def wrapper_out(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            before_args = args[:num_args]
            format_string = args[num_args]
            other_args = args[num_args+1:]
            string = format_string % other_args
            result = func(*before_args, string)
            return result
        return wrapper
    return wrapper_out


def TODO(func):
    _context = inspect.getframeinfo(inspect.currentframe().f_back, context=0)

    def THIS_FUNCTION_IS_NOT_YET_DONE(*args, **kwargs):
        print(_context)
        print("Sorry. The function '{}' is still in development".format(func.__name__))
        input("PRESS ENTER KEY TO QUIT")
        exit(0xFD)

    return THIS_FUNCTION_IS_NOT_YET_DONE
