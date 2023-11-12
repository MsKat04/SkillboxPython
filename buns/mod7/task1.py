def validate_args(func):
    def wrapper(*args):
        #количества аргументов
        if len(args) != 1:
            return "Not enough arguments" if len(args) < 1 else "Too many arguments"

        #тип аргумента
        if not isinstance(args[0], int):
            return "Wrong types"

        #отриц аргумент
        if args[0] < 0:
            return "Negative argument"

        return func(*args)

    return wrapper

@validate_args
def example_function(x):
    return f"Argument value: {x}"

print(example_function(1))
print(example_function(-1))
print(example_function("test"))
print(example_function(1, 2))