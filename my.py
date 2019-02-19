import sys
from subprocess import call

def dumpToInputfile():
	file = open("input.json", "w")
	for line in sys.stdin:
		file.write(line)
	file.close()

if __name__ == "__main__":
	dumpToInputfile()
	call(["python3", "mymodel.py"])
