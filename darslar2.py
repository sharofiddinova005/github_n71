def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Sharofiddinova")
        func(*args,**kwargs)
        print("Marjona")

    return wrapper

@my_decorator
def say_hello(a,b):
    print(a+b)
say_hello()

