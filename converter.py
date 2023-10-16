#!/usr/bin/env python3
c = 0
f = 0
# Converter module
# Converter from F < C
def temp_to_celsius(f):
    c = float((f - 32)* 5/9)
    return c
# Converter from C > F
def temp_to_farenheit(c):
    f = float((c * 9/5) + 32)
    return f
# Return either result 

