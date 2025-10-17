def greet_decorator(func):
    def wrapper():
        print("Hello! Welcome to Python.")
        func()
        print("Goodbye!")
    return wrapper

@greet_decorator
def say_name():
    print("My name is Arjun.")

say_name()
