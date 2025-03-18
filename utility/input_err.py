from functools import wraps

def input_error(func:"function")->"function":
    @wraps(func)
    def inner(*args, **kwargs):
        try:            
            return func(*args, **kwargs)
        
        except Exception as err:            
            return err
        
    return inner