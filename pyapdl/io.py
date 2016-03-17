# -*- coding: utf-8 -*-
from geometry import *

class Script(object):
    def __init__(self):
       self.__code = []
        
    def append(self,_str):
        if isinstance(_str,tuple) or isinstance(_str,list):
            for cd in _str:
                self.__code.append("%s\n"%(cd))
        else:
            self.__code.append("%s\n"%(_str))
        
    def save(self,filename):
        f = open(filename, "w")
        f.writelines(self.__code)
        f.close()

if __name__ == '__main__':
    pass
    