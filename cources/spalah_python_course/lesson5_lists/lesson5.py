#!/usr/bin/env python3

# chmod +x less4.py - make file executable

import sys

print(len(sys.argv))
print(sys.argv)
print(sys.argv[1])
print("Hello world")

if (len(sys.argv)) == 3:
    print(int(sys.argv[1]) + int(sys.argv[2]))
else:
    print("not correct param")



