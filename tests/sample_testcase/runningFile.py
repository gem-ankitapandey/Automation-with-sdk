from gempyp.gemPyp import GemPyp


obj = GemPyp()

obj.config = "C:\\Users\\an.pandey\\gempyp\\tests\\configTest\\Gempyp_Test_Suite.xml"
obj.MAIL = "ankitapandey281999@gmail.com"


# main condition is necessary
if __name__ == "__main__":
    obj.runner()