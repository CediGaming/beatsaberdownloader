import re

def promptSourceURL():
	print("Please provide the source (Web-)URL of the map to download:")
	url = input()
	if url.endswith('\\'):
		url = url[:-1]
	return url

def parseProviderFromURL(url: str):
	array = url.split('/')
	for item in array:
		regex = re.search('\w*\.\w*', item)
		if regex != None:
			if (item == "bsaber.com"):
				item = "beatsaver.com"
			return item
	
	return "Unknown.Domain"

def parseIdFromURL(url: str):
	array = url.split('/')
	out = ''
	i = -1
	while out == '':
		out = array[i]
		i = i - 1
	return out

def generateScrapeURL(provider: str, id: int):
	return f"https://{provider}/api/download/key/{id}"