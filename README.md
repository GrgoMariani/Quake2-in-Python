# Quake2 in Python
 A Quake2rantine project

## Current Status
Around 4% rewritten.

## Description
An attempt to rewrite the Quake2 source code to Python. Why? It's a good way to actually read through the code.

## Rules
* `Quick, not fast` - Q2 is heavily optimized in the right places, but we only care about transfering the logic here. If speed was an issue we would not have been using Python.
* `Quote the author` - One of the goals of this project is to try to use Python for it's readability, but still encourage people to read and possibly modify the original code afterwards. Try to make the code look as much as the original.
* `Question the code` - There's lots of unneeded parts of the code that may be simply skipped. We can simply `pass` them, but they should be left where they are (_check rule #2_). There is also a lot of code which is unnecessarily complicated here and solved a lot better with some simple pythonic code. Also don't forget that the original code is C and not C++.
* `Quest for perfection` - The ultimate goal is to make Q2 in python compatible with Q2 in C. This means that the network connection between them should also be working.
* `QrossPlatform`

## Completed files
q_shared, cvar, cd_win, m_flash
