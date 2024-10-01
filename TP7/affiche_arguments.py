#!/usr/bin/env python3

import sys

if len(sys.argv)==1:
    print("Usage :",sys.argv[0],"arg1 arg2 ... argN")
else:
    for i in sys.argv:
        print(i)