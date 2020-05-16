import inspect


def dynamically_create_function(name):
    frame, filename, line_number, function_name, lines, index = inspect.stack()[2]

    def created(*_, **__):
        print("{} is not yet linked".format(created.__name__))
        print("Line {} in {}".format(line_number, filename))
        input("PRESS ENTER KEY TO QUIT")
        exit(0xFD)

    created.__name__ = name
    return created


def LinkEmptyFunctions(globals_pointer, empty_function_names_list):
    for name in empty_function_names_list:
        globals_pointer[name] = dynamically_create_function(name)


"""
    The linker is a bit complicated machine. Since we are emulating the programming style of C-development it can be
    somewhat tricky to finally link these functions in the end. This is why we create empty placeholders for most
    of the outside-linked functions in every namespace and replace them in the end with the real values.
    
    In short: this resolves circular dependencies we might run into.
    
"""