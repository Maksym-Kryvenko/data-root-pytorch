# Implement decorator which returns function signature and it's return value
def debug(func):
    """
    :param func: function
    """
    # YOUR CODE HERE
    def wrapper(*args):
        args_str = ', '.join(map(str, args))
        result = func(*args)
        return f"{func.__name__}({args_str}) was called and returned {result}"
    return wrapper

@debug
def add(a, b):
    return a + b
    
@debug
def sub(a, b=100):
    return a - b

print(add(3, 4))
print(sub(3))
print(sub(3,4))

# Results:
# add(3, 4) was called and returned 7
# sub(3) was called and returned -97
# sub(3, 4) was called and returned -1