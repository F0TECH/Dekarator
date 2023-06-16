def cast(typ):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                result = typ(result)
            except (TypeError, ValueError):
                pass
            return result
        return wrapper
    return decorator

@cast(float)
def divide(x, y):
    return x / y

result = divide(10, 4)
print(result, type(result))