import sys;
import mmlibrary as mm;

def mymodel():
	first = mm.getArgument("first")
	second = mm.getArgument("second")
	return first + second

def dumpToInputfile():
	file = open("input.json", "w")
	for line in sys.stdin:
		file.write(line)
	file.close()

if __name__ == "__main__":
	dumpToInputfile()
	
	res = mymodel()

	mm.returnScore(res)
