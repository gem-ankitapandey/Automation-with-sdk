from gempyp.gemPyp import Gempyp
import sys
import os


obj = Gempyp()

"""Giving the default config file location  and default mail"""

obj.config = ""
obj.MAIL = "8979149361t@gmail.com"


# main condition is necessary
if __name__ == "__main__":
    print(obj.__dict__)
    obj.runner()