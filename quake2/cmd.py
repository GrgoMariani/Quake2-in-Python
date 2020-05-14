cmd_argv = []


def Cmd_Argc():
    return len(cmd_argv)


def Cmd_Argv(arg):
    if arg >= len(cmd_argv):
        return ""
    return cmd_argv[0]


def Cmd_AddCommand(cmd_name, function):

    pass
