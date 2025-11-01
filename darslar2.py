def my_decorator(f):
    def wrapper(*args,**kwargs):
        print("najot ta'lim")
        f(*args,**kwargs)
        print("n71")

    return wrapper

@my_decorator
def say_hello(a,b):
    print(a+b)
say_hello(10,5)

