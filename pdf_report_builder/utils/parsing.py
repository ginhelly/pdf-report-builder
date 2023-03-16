
def continue_on_key_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, *kwargs)
        except KeyError:
            pass
    return wrapper