from RobokitRS import * 
import time as t
rs = RobokitRS.RobokitRS()
rs.port_open("com3")
def d1():
    rs.set_dotmatrix_row_all(["111111111111111",
                              "000000111000000",
                              "000000111000000",
                              "000000111000000",
                              "000000111000000",
                              "000000111000000",
                              "111111111111111"])
    t.sleep(1)
    rs.clear_dotmatrix()
d1()