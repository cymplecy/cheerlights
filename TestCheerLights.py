__author__ = 'Simon'

import cheerlights
import time

clights = cheerlights.CheerLights()
while True:
    print clights.get_colours()
    time.sleep(4)
