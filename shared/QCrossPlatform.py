import ctypes


def MessageBox(num, title, text, style):
    return ctypes.windll.user32.MessageBoxW(num, text, title, style)

