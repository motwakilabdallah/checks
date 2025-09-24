#!/usr/bin/env python3
import os
import sys
def check_reboot():
	"""returns True if the computer has a pending reboot"""
	return os.path.exist("/run/reboot-required")

def main():

	if check_reboot():
		print("Pending Reboot")
		sys.exist(1)
	if disk_full():
		print("Disk Full")
		sys.exist(1)
		print("everything is ok.")
		sys.exist(0)
main()
