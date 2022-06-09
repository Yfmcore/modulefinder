# prototype project by @yfimsky
# version 1.2 alpha

import importlib

def getmodule():

    inp = input("Write module to enable: ")
    importlib.import_module(inp)
        
getmodule()