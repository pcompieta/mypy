import sys
from subprocess import call

def dumpInputToJsonFile():
	file = open("input.json", "w")
	for line in sys.stdin:
		file.write(line)
	file.close()

if __name__ == "__main__":
	dumpInputToJsonFile()
	call(["python3", "model.py"])
