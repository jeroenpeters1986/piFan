#!/usr/bin/python
import json
import shlex
import subprocess
import time

pifan_path = "/home/pi/pifan/"

with open("{}data/curr_threshold.json".format(pifan_path), 'r') as json_file:    
    curr_threshold = float(json.load(json_file).get('temperature'))

with open("{}data/curr_temp.json".format(pifan_path), 'r') as json_file:    
    curr_temp = float(json.load(json_file).get('temperature'))

# ./hub-ctrl -h 0 -P 2 -p 0
switch = 0
if curr_temp > curr_threshold:
    switch = 1

control_command = "sudo {}hub-ctrl -h 1 -P 2 -p {}"
complete_control_command = shlex.split(control_command.format(pifan_path, str(switch)))
subprocess.call(complete_control_command)

time.sleep(15)
