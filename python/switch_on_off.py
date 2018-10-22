#!/usr/bin/python
import json
import re
import shlex
import subprocess
import time

pifan_path = "/home/pi/pifan/"

with open("{}data/curr_threshold.json".format(pifan_path), 'r') as json_file:
    curr_threshold = float(json.load(json_file).get('temperature'))

with open("{}data/curr_temp.json".format(pifan_path), 'r') as json_file:
    curr_temp = float(json.load(json_file).get('temperature'))

# Determine CPU revision for Pi compatibility
cpu_revision = "pi"
command = "cat /proc/cpuinfo"
all_info = subprocess.check_output(command, shell=True).strip()
for line in all_info.split("\n"):
    if "Revision" in line:
        cpu_revision = re.sub(".*Revision.*:", "", line, 1).strip()

# ./hub-ctrl -h 0 -P 2 -p 0
switch = 0
if curr_temp > curr_threshold:
    switch = 1

usb_hub_id = 0
if cpu_revision == "a020d3":
    usb_hub_id = 1

control_command = "sudo {}hub-ctrl -h {} -P 2 -p {}"
complete_control_command = shlex.split(control_command.format(pifan_path, str(usb_hub_id), str(switch)))
subprocess.call(complete_control_command)

time.sleep(15)
