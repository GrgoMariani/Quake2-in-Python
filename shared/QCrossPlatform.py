import ctypes  # An included library with Python install.


def MessageBox(num, title, text, style):
    return ctypes.windll.user32.MessageBoxW(num, text, title, style)

