import sys, json;

json_file = open("input.json")
json_data = json_file.read()
inputs = json.loads(json_data)
json_file.close()

def getArgument(name):
	return inputs[name]

def returnScore(score):
	scoreMap = { "score" : score }
	print(json.dumps(scoreMap))
