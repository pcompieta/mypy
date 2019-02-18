import sys, json;

# both these functions are defined in a 'mmlibrary.py' file

def getArgument(name):
	json_file = open("input.json")
	json_data = json_file.read()
	inputs = json.loads(json_data)
	json_file.close()
	return inputs[name]

def returnScore(score):
    print(json.dumps(score))

def dumpToInputfile():
	file = open("input.json", "w")
	for line in sys.stdin:
		file.write(line)
	file.close()

# both these functions are defined in a 'mmlibrary.py' file

def mymodel():
	first = getArgument("first")
	second = getArgument("second")
	return first + second

if __name__ == "__main__":
	dumpToInputfile()
	
	res = mymodel()
	
	returnScore(res)
