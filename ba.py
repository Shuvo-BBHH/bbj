import os, sys
try:
    __import__("c").__niki__()
except Exception as e:
    exit(str(e))
