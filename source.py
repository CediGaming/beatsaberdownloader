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
			return item
	
	return "Unknown.Domain"

def parseIdFromURL(url: str):
	array = url.split('/')
	
	return int(array[-1])

def generateScrapeURL(provider: str, id: int):
	return f"https://{provider}/api/download/key/{id}"