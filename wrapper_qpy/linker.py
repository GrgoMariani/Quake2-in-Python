def dynamically_create_function(name):
    def created(**_):
        print(created.__name__, " is not yet linked")
        exit(1)
    created.__name__ = name
    return created


def LinkEmptyFunction(globals_pointer, name):
    globals_pointer[name] = dynamically_create_function(name)


def LinkEmptyFunctions(globals_pointer, empty_function_names_list):
    for name in empty_function_names_list:
        LinkEmptyFunction(globals_pointer, name)
