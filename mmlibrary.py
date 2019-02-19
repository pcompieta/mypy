import sys, json;

def getArgument(name):
	json_file = open("input.json")
	json_data = json_file.read()
	inputs = json.loads(json_data)
	json_file.close()
	return inputs[name]

def returnScore(score):
	scoreMap ={ "score": score }
	print(json.dumps(scoreMap))
