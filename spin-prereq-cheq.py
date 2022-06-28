#!/usr/bin/python3

import json, sys

def main():
	files = init()
	for fn in files:
		print(f"Checking '{fn}'...")
		with open(fn, "r") as f:
			contents = json.load(f)
		stages = contents["stages"]
		missing = check(stages)
		if missing == 0:
			print("\tAll good!")


def check(stages):
	# first get all the refIds
	refIds = []
	for stage in stages:
		if 'refId' not in stage:
			continue
		refIds.append(stage['refId'])
	# then make sure no stage has a pre-req we haven't seen
	missing = 0
	for stage in stages:
		if not "requisiteStageRefIds" in stage:
			continue
		for prereq in stage["requisiteStageRefIds"]:
			if prereq not in refIds:
				missing += 1
				print(f"\tStage with refId '{stage['refId']}' has requisiteStageRefId '{prereq}', which is not found.")
	return missing


def init():
	if len(sys.argv) < 2:
		print("Which file(s) do you want me to check?")
		sys.exit(0)
	files = sys.argv[1:]
	return files


if __name__ == "__main__":
	main()
