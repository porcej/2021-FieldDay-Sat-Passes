#!/usr/bin/env python3

from os import listdir, path
from os.path import isfile, join

def readPredictionFile(file):
	f = open(file, "r")
	sat_passes = {
		"satellite": "",
		"passes": [],
	}
	lines = f.readlines()
	for line in lines:
		[title, *data] = line.split(":", 1)
		if title == "MacDoppler Predictions":
			sat_passes["satellite"] = data[0].strip()
		elif title == "Rise":
			[date, time, az, el, *other] = data[0].strip().split()
			sat_passes['passes'].append({'start_date': date, "start_time": time})
		elif title == "Max":
			[date, time, az, el, *other] = data[0].strip().split()
			sat_passes["passes"][-1]["max_el"] = el
		elif title == "Set":
			[date, time, az, el, *other] = data[0].strip().split()
			sat_passes["passes"][-1]["end_date"] = date
			sat_passes["passes"][-1]["end_time"] = time[-1]

			print(sat_passes["passes"][-1])
		# print(title)

cwd = path.dirname(path.realpath(__file__))


onlyfiles = [f for f in listdir(cwd) if (f.endswith(".txt") and isfile(join(cwd, f)))]

for file in onlyfiles:
	print(file)
# print(onlyfiles)
file = onlyfiles[1]
f = readPredictionFile(join(cwd, file))



