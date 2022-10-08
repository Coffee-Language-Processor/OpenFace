#!/usr/bin/env python

import math
from subprocess import Popen, DEVNULL
import shlex
import os
import errno
import time
import glob

# Constants for later use
of2_verbose = False
temp_output = "of2_out"
temp_output_file = temp_output + '.csv'
landmark_count = 68

# This line finds the openface software
# If you're getting an error here, make sure this file is in the same folder as your openface installation
exe = ([exe for exe in glob.glob("./**/FeatureExtraction", recursive=True) if os.path.isfile(exe)
       ]+[exe for exe in glob.glob(".\\**\\FeatureExtraction.exe", recursive=True)])[0]

# Clean up the temp file from a previous run, if it exists
try:
	os.remove(temp_output_file)
except OSError as e:
	if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
		raise  # re-raise exception if a different error occurred

# These lines write the command to run openface with the correct options
command = shlex.split(" -device 0 -out_dir . -pose -2Dfp -of "+temp_output)
command.insert(0, exe)

# This line starts openface
of2 = Popen(command, stdin=DEVNULL, stdout=(
    None if of2_verbose else DEVNULL), stderr=DEVNULL)

# This loop waits until openface has actually started, as it can take some time to start producing output
while not os.path.exists(temp_output_file):
	time.sleep(.5)

# Openface saves info to a file, and we open that file here
data = open(temp_output_file, 'r')

# This loop repeats while openface is still running
# Inside the loop, we read from the file that openface outputs to and check to see if there's anything new
# We handle the data if there is any, and wait otherwise
Globals = [0] * 4 # Finds out if data is changing or not
print(Globals)
while (of2.poll() == None):
	line = data.readline().strip()
	if (line != ""):
		try:

			# Parse the line and save the useful values
			of_values = [float(v) for v in line.split(',')]
			print(len(of_values))
			timestamp, confidence, success = of_values[2:5]
			pitch, yaw, roll = of_values[8:11]
		    
			if len(of_values) == 147:
				landmarks = []
				for i in range(11, landmark_count + 11):
					print(i, i+landmark_count)
					landmarks.append((of_values[i], of_values[i+landmark_count]))

				print(math.dist(landmarks[48],landmarks[54]))
				# Globals[4] = landmarks[48] 
				# Globals[5] = landmarks[54]
		except ValueError:
			# This exception handles the header line
			continue
			
        # ********************************************
		# Most, maybe all, of your code will go here
		# ********************************************
		
		if abs(Globals[0] - timestamp) < 1:
			Globals[0] = timestamp
			if abs(Globals[1] - yaw) >	0.08:
				print("Shaking no\n")
				Globals[1] = yaw

			if abs(Globals[2] - roll) > .11:
				print("\'Indian nod\'\n")
				Globals[2] = roll
			
			if abs(Globals[3] - pitch) > 0.08:
				print("Nodding yes\n")
				Globals[3]= pitch


		
		# Replace this line
		
	
		
	else:
		time.sleep(.01)
	
# Reminder: press 'q' to exit openface

print("Program ended")

data.close()
