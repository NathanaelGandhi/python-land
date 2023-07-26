def my_function():
    print("Hello world!")


# How to create runnable Python modules
def greeter():
    print("Hello from mymodule.py")


# How to create runnable Python modules
# Only call the greeter when run as
# a script (with python mymodule.py)
if __name__ == "__main__":
    greeter()
