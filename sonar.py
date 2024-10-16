import time as t
import random
from RobokitRS import *
rs = RobokitRS.RobokitRS()
rs.port_open("com3")
rs.sonar_begin(2)

for i in range(10):
    SONAR = rs.sonar_read(2)
    print(SONAR)
    t.sleep(1)