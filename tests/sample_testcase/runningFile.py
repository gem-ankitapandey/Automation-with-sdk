from gempyp.gemPyp import Gempyp
import sys
import os


obj = Gempyp()


obj.config = "C:\\Users\\ta.agarwal\\gempyp\\tests\\configTest\\Gempyp_Test_suite.xml"
obj.MAIL = "8979149361t@gmail.com"


# main condition is necessary
if __name__ == "__main__":
    print(obj.__dict__)
    obj.runner()