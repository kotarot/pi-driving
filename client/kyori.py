#!/usr/bin/env python
# 

import spidev
import time
import subprocess

spi = spidev.SpiDev()	
spi.open(0, 0)

#try:
cfg_time = 0.2
cfg_count = 1

sumVal = 0
counter = 0
while True:
	resp = spi.xfer2([0x68, 0x00])
	value = (resp[0] * 256 + resp[1]) & 0x3ff

	if counter == cfg_count:
		print sumVal/cfg_count
		sumVal = 0
		counter = 0
	else:
		sumVal += value
		counter+=1

	time.sleep(cfg_time)

#except KyboardInterrupt:
spi.close()

